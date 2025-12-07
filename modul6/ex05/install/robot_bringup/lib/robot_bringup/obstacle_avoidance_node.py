#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist
from cv_bridge import CvBridge
import cv2
import numpy as np


class WallAvoidanceNode(Node):
    def __init__(self):
        super().__init__('wall_avoidance_node')
        
        # Подписка на изображение глубины
        self.depth_subscription = self.create_subscription(
            Image,
            '/depth/image',
            self.depth_callback,
            10
        )
        
        # Публикатор для управления роботом
        self.cmd_pub = self.create_publisher(
            Twist,
            '/robot/cmd_vel',
            10
        )
        
        self.br = CvBridge()
        
        # Параметры управления
        self.safe_distance = 0.5  # Минимальное безопасное расстояние до стены (в метрах)
        self.max_linear_speed = 0.2  # Максимальная линейная скорость
        self.max_angular_speed = 0.5  # Максимальная угловая скорость
        self.wall_detected = False
        self.obstacle_in_front = False
        
        # Для визуализации
        self.visualize = True
        
        self.get_logger().info('Wall avoidance node started')
        self.get_logger().info(f'Safe distance: {self.safe_distance}m')
        
        # Таймер для публикации команд управления
        self.timer = self.create_timer(0.1, self.publish_cmd_vel)
        
    def depth_callback(self, msg):
        try:
            # Преобразуем ROS сообщение в массив numpy
            cv_image = self.br.imgmsg_to_cv2(msg, desired_encoding='passthrough')
            depth_array = np.array(cv_image, dtype=np.float32)
            
            # Обрабатываем данные глубины
            self.process_depth_data(depth_array, msg.width, msg.height)
            
            # Визуализация (опционально)
            if self.visualize:
                self.visualize_depth(depth_array)
                
        except Exception as e:
            self.get_logger().error(f'Error processing depth image: {e}')
    
    def process_depth_data(self, depth_array, width, height):
        """
        Анализирует данные глубины для обнаружения препятствий
        """
        # Маскируем невалидные значения (0 или очень большие значения)
        valid_mask = (depth_array > 0.1) & (depth_array < 10.0)
        
        if not np.any(valid_mask):
            self.obstacle_in_front = False
            return
        
        # Берем центральную область изображения для обнаружения препятствий впереди
        center_region = depth_array[height//3:2*height//3, width//3:2*width//3]
        valid_center = center_region[(center_region > 0.1) & (center_region < 10.0)]
        
        if valid_center.size == 0:
            self.obstacle_in_front = False
            return
        
        # Находим минимальное расстояние в центральной области
        min_distance = np.min(valid_center)
        
        # Проверяем, есть ли препятствие ближе безопасного расстояния
        if min_distance < self.safe_distance:
            self.obstacle_in_front = True
            self.get_logger().warn(
                f'Obstacle detected at {min_distance:.2f}m '
                f'(< safe distance {self.safe_distance}m)'
            )
        else:
            self.obstacle_in_front = False
    
    def publish_cmd_vel(self):
        """
        Публикует команды управления в зависимости от наличия препятствий
        """
        cmd_msg = Twist()
        
        if self.obstacle_in_front:
            # Если препятствие обнаружено - останавливаем робота
            cmd_msg.linear.x = 0.0
            cmd_msg.angular.z = 0.0
            
            # Можно добавить вращение на месте для поиска пути
            # cmd_msg.angular.z = 0.3
            
            self.wall_detected = True
        else:
            # Если препятствий нет - двигаемся вперед
            cmd_msg.linear.x = self.max_linear_speed
            cmd_msg.angular.z = 0.0
            self.wall_detected = False
        
        # Публикуем команду
        self.cmd_pub.publish(cmd_msg)
        
        # Логируем состояние (не слишком часто)
        if hasattr(self, 'last_log_time'):
            import time
            current_time = time.time()
            if current_time - self.last_log_time > 2.0:  # Логируем каждые 2 секунды
                if self.wall_detected:
                    self.get_logger().info('Wall detected - stopping robot')
                else:
                    self.get_logger().info('No wall detected - moving forward')
                self.last_log_time = current_time
        else:
            self.last_log_time = time.time()
    
    def visualize_depth(self, depth_array):
        """
        Визуализация данных глубины для отладки
        """
        # Нормализуем для отображения
        depth_display = cv2.normalize(
            depth_array, None, 0, 255, cv2.NORM_MINMAX
        ).astype(np.uint8)
        
        # Применяем цветовую карту
        depth_colored = cv2.applyColorMap(depth_display, cv2.COLORMAP_JET)
        
        # Добавляем информацию о расстоянии
        if self.obstacle_in_front:
            cv2.putText(
                depth_colored,
                f'STOP! Obstacle: {np.min(depth_array[depth_array>0]):.2f}m',
                (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 0, 255),
                2
            )
            # Добавляем красный прямоугольник в центральной области
            h, w = depth_array.shape
            cv2.rectangle(
                depth_colored,
                (w//3, h//3),
                (2*w//3, 2*h//3),
                (0, 0, 255),
                2
            )
        else:
            cv2.putText(
                depth_colored,
                f'Moving forward',
                (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 0),
                2
            )
            # Добавляем зеленый прямоугольник в центральной области
            h, w = depth_array.shape
            cv2.rectangle(
                depth_colored,
                (w//3, h//3),
                (2*w//3, 2*h//3),
                (0, 255, 0),
                2
            )
        
        # Показываем изображение
        cv2.imshow('Depth Camera (Wall Avoidance)', depth_colored)
        cv2.waitKey(1)


def main(args=None):
    rclpy.init(args=args)
    
    # Создаем узел
    node = WallAvoidanceNode()
    
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Shutting down wall avoidance node...')
    finally:
        # Останавливаем робота при завершении
        stop_msg = Twist()
        stop_msg.linear.x = 0.0
        stop_msg.angular.z = 0.0
        node.cmd_pub.publish(stop_msg)
        
        cv2.destroyAllWindows()
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()