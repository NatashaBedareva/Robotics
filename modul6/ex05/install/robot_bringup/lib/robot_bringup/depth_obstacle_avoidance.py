#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image, PointCloud2, CameraInfo
from geometry_msgs.msg import Twist
import numpy as np
from cv_bridge import CvBridge
import struct
from rclpy.qos import QoSProfile, ReliabilityPolicy

class DepthObstacleAvoidance(Node):
    def __init__(self):
        super().__init__('depth_obstacle_avoidance')
        
        # Параметры
        self.declare_parameter('obstacle_distance', 1.0)  # метры
        self.declare_parameter('min_height', 0.1)  # метры
        self.declare_parameter('max_height', 0.5)  # метры
        self.declare_parameter('center_region', 0.3)  # центральная область (0-1)
        self.declare_parameter('stop_timeout', 2.0)  # секунды ожидания после остановки
        
        self.obstacle_distance = self.get_parameter('obstacle_distance').value
        self.min_height = self.get_parameter('min_height').value
        self.max_height = self.get_parameter('max_height').value
        self.center_region = self.get_parameter('center_region').value
        self.stop_timeout = self.get_parameter('stop_timeout').value
        
        self.get_logger().info(f'Obstacle avoidance initialized with:')
        self.get_logger().info(f'  Distance threshold: {self.obstacle_distance}m')
        self.get_logger().info(f'  Height range: {self.min_height}-{self.max_height}m')
        
        # Инициализация
        self.bridge = CvBridge()
        self.camera_info = None
        self.camera_matrix = None
        self.distortion_coeffs = None
        self.obstacle_detected = False
        self.last_stop_time = None
        self.current_cmd_vel = Twist()
        
        # Подписка на топики
        qos_profile = QoSProfile(depth=10, reliability=ReliabilityPolicy.BEST_EFFORT)
        
        # Подписка на данные глубины (изображение)
        self.depth_image_sub = self.create_subscription(
            Image,
            '/depth/image',
            self.depth_image_callback,
            qos_profile
        )
        
        # Подписка на облако точек (альтернативный вариант)
        self.pointcloud_sub = self.create_subscription(
            PointCloud2,
            '/depth/points',
            self.pointcloud_callback,
            qos_profile
        )
        
        # Подписка на информацию о камере
        self.camera_info_sub = self.create_subscription(
            CameraInfo,
            '/depth/camera_info',
            self.camera_info_callback,
            10
        )
        
        # Подписка на текущую команду скорости
        self.cmd_vel_sub = self.create_subscription(
            Twist,
            '/robot/cmd_vel',
            self.cmd_vel_callback,
            10
        )
        
        # Публикация модифицированной команды скорости
        self.cmd_vel_pub = self.create_publisher(
            Twist,
            '/robot/cmd_vel',
            10
        )
        
        # Таймер для публикации команд
        self.timer = self.create_timer(0.1, self.publish_cmd_vel)
        
        self.get_logger().info('Depth obstacle avoidance node started')
    
    def camera_info_callback(self, msg):
        """Обработка информации о камере"""
        if self.camera_info is None:
            self.camera_info = msg
            self.camera_matrix = np.array(msg.k).reshape(3, 3)
            self.distortion_coeffs = np.array(msg.d)
            self.get_logger().info('Camera info received')
    
    def cmd_vel_callback(self, msg):
        """Сохранение текущей команды скорости"""
        self.current_cmd_vel = msg
    
    def depth_image_callback(self, msg):
        """Обработка изображения глубины"""
        try:
            # Конвертация изображения в numpy массив
            depth_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='32FC1')
            
            # Получение размеров изображения
            height, width = depth_image.shape
            
            # Определение центральной области
            center_start = int(width * (0.5 - self.center_region/2))
            center_end = int(width * (0.5 + self.center_region/2))
            
            # Выделение центральной полосы изображения
            center_region = depth_image[:, center_start:center_end]
            
            # Фильтрация валидных значений (не NaN и не Inf)
            valid_depths = center_region[np.isfinite(center_region)]
            
            if len(valid_depths) > 0:
                # Находим минимальное расстояние в центральной области
                min_distance = np.min(valid_depths)
                
                # Проверка на препятствие
                if min_distance < self.obstacle_distance and min_distance > 0:
                    if not self.obstacle_detected:
                        self.get_logger().warn(f'Obstacle detected at {min_distance:.2f}m')
                        self.obstacle_detected = True
                        self.last_stop_time = self.get_clock().now()
                else:
                    if self.obstacle_detected:
                        # Проверка таймаута после обнаружения препятствия
                        if self.last_stop_time:
                            elapsed = (self.get_clock().now() - self.last_stop_time).nanoseconds * 1e-9
                            if elapsed > self.stop_timeout:
                                self.get_logger().info('Obstacle cleared, resuming movement')
                                self.obstacle_detected = False
                        else:
                            self.obstacle_detected = False
                
                # Отладочная информация
                self.get_logger().debug(f'Min distance: {min_distance:.2f}m, Obstacle: {self.obstacle_detected}')
            
        except Exception as e:
            self.get_logger().error(f'Error processing depth image: {str(e)}')
    
    def pointcloud_callback(self, msg):
        """Альтернативная обработка через облако точек (более точная)"""
        try:
            # Преобразование облака точек в массив
            points = self.pointcloud2_to_array(msg)
            
            if len(points) > 0:
                # Фильтрация точек по высоте
                height_filtered = points[
                    (points[:, 2] > self.min_height) & 
                    (points[:, 2] < self.max_height)
                ]
                
                if len(height_filtered) > 0:
                    # Вычисление расстояния до точек (x - вперед, y - влево/вправо, z - вверх/вниз)
                    distances = np.sqrt(height_filtered[:, 0]**2 + height_filtered[:, 1]**2)
                    
                    # Фильтрация точек в центральной области по оси Y
                    y_range = self.obstacle_distance * np.tan(np.radians(30)) * self.center_region
                    center_filtered = height_filtered[np.abs(height_filtered[:, 1]) < y_range]
                    
                    if len(center_filtered) > 0:
                        # Вычисление расстояний до центральных точек
                        center_distances = np.sqrt(center_filtered[:, 0]**2 + center_filtered[:, 1]**2)
                        min_distance = np.min(center_distances)
                        
                        # Проверка на препятствие
                        if min_distance < self.obstacle_distance and min_distance > 0:
                            if not self.obstacle_detected:
                                self.get_logger().warn(f'Obstacle detected at {min_distance:.2f}m (pointcloud)')
                                self.obstacle_detected = True
                                self.last_stop_time = self.get_clock().now()
                        else:
                            if self.obstacle_detected:
                                if self.last_stop_time:
                                    elapsed = (self.get_clock().now() - self.last_stop_time).nanoseconds * 1e-9
                                    if elapsed > self.stop_timeout:
                                        self.get_logger().info('Obstacle cleared (pointcloud)')
                                        self.obstacle_detected = False
                                else:
                                    self.obstacle_detected = False
        
        except Exception as e:
            self.get_logger().error(f'Error processing pointcloud: {str(e)}')
    
    def pointcloud2_to_array(self, cloud_msg):
        """Конвертация PointCloud2 в numpy массив"""
        # Получаем смещения полей
        x_offset = None
        y_offset = None
        z_offset = None
        
        for field in cloud_msg.fields:
            if field.name == 'x':
                x_offset = field.offset
            elif field.name == 'y':
                y_offset = field.offset
            elif field.name == 'z':
                z_offset = field.offset
        
        if None in [x_offset, y_offset, z_offset]:
            return np.array([])
        
        # Конвертируем данные
        points = []
        point_step = cloud_msg.point_step
        
        for i in range(cloud_msg.width * cloud_msg.height):
            base = i * point_step
            
            try:
                x = struct.unpack('f', cloud_msg.data[base + x_offset:base + x_offset + 4])[0]
                y = struct.unpack('f', cloud_msg.data[base + y_offset:base + y_offset + 4])[0]
                z = struct.unpack('f', cloud_msg.data[base + z_offset:base + z_offset + 4])[0]
                
                # Проверка на валидные значения
                if np.isfinite(x) and np.isfinite(y) and np.isfinite(z):
                    points.append([x, y, z])
            except:
                continue
        
        return np.array(points)
    
    def publish_cmd_vel(self):
        """Публикация модифицированной команды скорости"""
        cmd_vel = Twist()
        
        if self.obstacle_detected:
            # Если обнаружено препятствие, останавливаем робота
            cmd_vel.linear.x = 0.0
            cmd_vel.angular.z = 0.0
            self.get_logger().debug('Stopping robot due to obstacle')
        else:
            # Иначе передаем оригинальную команду
            cmd_vel = self.current_cmd_vel
        
        self.cmd_vel_pub.publish(cmd_vel)

def main(args=None):
    rclpy.init(args=args)
    node = DepthObstacleAvoidance()
    
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()