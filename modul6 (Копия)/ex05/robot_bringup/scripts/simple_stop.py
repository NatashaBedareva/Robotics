#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import PointCloud2
from geometry_msgs.msg import Twist
import struct
from rclpy.qos import QoSProfile, ReliabilityPolicy
import numpy as np

class SimpleObstacleStop(Node):
    def __init__(self):
        super().__init__('simple_obstacle_stop')
        
        self.declare_parameter('stop_distance', 1.5)     
        self.declare_parameter('forward_speed', 0.3)      
        self.declare_parameter('min_height', 0.2)        
        self.declare_parameter('max_height', 1.0)         
        self.declare_parameter('min_points_threshold', 10) #
        
        self.stop_distance = self.get_parameter('stop_distance').value
        self.forward_speed = self.get_parameter('forward_speed').value
        self.min_height = self.get_parameter('min_height').value
        self.max_height = self.get_parameter('max_height').value
        self.min_points = self.get_parameter('min_points_threshold').value
        
        self.get_logger().info('=== Простой детектор препятствий ===')
        self.get_logger().info(f'Скорость: {self.forward_speed} м/с')
        self.get_logger().info(f'Дистанция остановки: {self.stop_distance} м')
        self.get_logger().info(f'Высота объектов: {self.min_height}-{self.max_height} м')
        self.get_logger().info(f'Минимум точек: {self.min_points}')
        

        self.obstacle_detected = False
        

        qos_profile = QoSProfile(depth=10, reliability=ReliabilityPolicy.BEST_EFFORT)
        self.pc_sub = self.create_subscription(
            PointCloud2,
            '/depth/points',
            self.pointcloud_callback,
            qos_profile
        )
        

        self.cmd_pub = self.create_publisher(Twist, '/robot/cmd_vel', 10)

        self.timer = self.create_timer(0.1, self.publish_cmd)
        
        self.get_logger().info('Робот начал движение!')
        self.get_logger().info('Чтобы остановить: Ctrl+C')
    
    def pointcloud_callback(self, msg):

        try:

            x_offset = y_offset = z_offset = None
            
            for field in msg.fields:
                if field.name == 'x':
                    x_offset = field.offset
                elif field.name == 'y':
                    y_offset = field.offset
                elif field.name == 'z':
                    z_offset = field.offset
            
            if None in [x_offset, y_offset, z_offset]:
                return
            
            point_step = msg.point_step
            min_distance = float('inf')
            obstacle_count = 0
            
            total_points = min(msg.width * msg.height, 10000)
            
            for i in range(0, total_points, 3):  
                base = i * point_step
                
                try:

                    x = struct.unpack('f', msg.data[base + x_offset:base + x_offset + 4])[0]
                    y = struct.unpack('f', msg.data[base + y_offset:base + y_offset + 4])[0]
                    z = struct.unpack('f', msg.data[base + z_offset:base + z_offset + 4])[0]

                    if not (np.isfinite(x) and np.isfinite(y) and np.isfinite(z)):
                        continue
                    
                  
                    if self.min_height < z < self.max_height:

                        if abs(y) < 0.5: 
                            distance = (x**2 + y**2)**0.5

                            if 0.3 < distance < self.stop_distance:
                                obstacle_count += 1
                                if distance < min_distance:
                                    min_distance = distance
                                    
                except:
                    continue
            

            self.process_detection(min_distance, obstacle_count)
            
        except Exception as e:
            self.get_logger().error(f'Ошибка обработки облака точек: {str(e)}')
    
    def process_detection(self, min_distance, obstacle_count):
        """Обработка результатов обнаружения препятствий"""
        if min_distance < float('inf') and obstacle_count >= self.min_points:
            if min_distance < self.stop_distance:
                if not self.obstacle_detected:
                    self.obstacle_detected = True
                    self.get_logger().warn(f'⚠️  ПРЕПЯТСТВИЕ! {min_distance:.2f} м, точек: {obstacle_count}')
            else:
                if self.obstacle_detected:
                    self.obstacle_detected = False
                    self.get_logger().info('✅ Путь свободен')
        else:
            if self.obstacle_detected:
                self.obstacle_detected = False
        
        if hasattr(self, 'last_log_time'):
            elapsed = (self.get_clock().now() - self.last_log_time).nanoseconds * 1e-9
            if elapsed > 2.0:
                status = "⛔ ОСТАНОВЛЕН" if self.obstacle_detected else "▶️  ДВИЖЕТСЯ"
                dist_info = f", ближайший: {min_distance:.2f} м" if min_distance < float('inf') else ""
                self.get_logger().info(f'Статус: {status}{dist_info}')
                self.last_log_time = self.get_clock().now()
        else:
            self.last_log_time = self.get_clock().now()
    
    def publish_cmd(self):
        """Публикация команды скорости"""
        cmd = Twist()
        
        if self.obstacle_detected:

            cmd.linear.x = 0.0
            cmd.angular.z = 0.0
        else:

            cmd.linear.x = self.forward_speed
            cmd.angular.z = 0.0
        
        self.cmd_pub.publish(cmd)

def main(args=None):
    rclpy.init(args=args)
    node = SimpleObstacleStop()
    
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:

        stop_cmd = Twist()
        node.cmd_pub.publish(stop_cmd)
        node.get_logger().info('Остановка по команде пользователя...')
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()