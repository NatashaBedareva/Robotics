#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist
import struct
import array
from rclpy.qos import QoSProfile, ReliabilityPolicy

class SimpleObstacleStop(Node):
    def __init__(self):
        super().__init__('simple_obstacle_stop')
        
        # Параметры
        self.declare_parameter('stop_distance', 1.5)  # дистанция остановки (метры)
        self.declare_parameter('forward_speed', 0.3)  # скорость движения вперед (м/с)
        
        self.stop_distance = self.get_parameter('stop_distance').value
        self.forward_speed = self.get_parameter('forward_speed').value
        
        self.get_logger().info('=== Простой детектор препятствий ===')
        self.get_logger().info(f'Робот движется со скоростью: {self.forward_speed} м/с')
        self.get_logger().info(f'Останавливается при препятствии ближе: {self.stop_distance} м')
        
        # Флаг препятствия
        self.obstacle_detected = False
        
        # Подписка на изображение глубины
        qos_profile = QoSProfile(depth=10, reliability=ReliabilityPolicy.BEST_EFFORT)
        self.depth_sub = self.create_subscription(
            Image,
            '/depth/image',
            self.depth_callback,
            qos_profile
        )
        
        # Публикатор команд скорости
        self.cmd_pub = self.create_publisher(Twist, '/robot/cmd_vel', 10)
        
        # Таймер для публикации скорости
        self.timer = self.create_timer(0.1, self.publish_cmd)
        
        self.get_logger().info('Робот начал движение!')
    
    def depth_callback(self, msg):
        """Обработка данных глубины"""
        try:
            # Проверяем формат (ожидаем 32FC1 - float32)
            if msg.encoding != '32FC1':
                self.get_logger().warn(f'Неожиданный формат: {msg.encoding}')
                return
            
            # Разбираем данные глубины
            point_step = 4  # 4 байта на float32
            min_distance = float('inf')
            
            # Анализируем только центральные строки (игнорируем верх и низ)
            start_row = msg.height // 3
            end_row = 2 * msg.height // 3
            
            # Анализируем только центральные 40% по ширине
            start_col = int(msg.width * 0.3)
            end_col = int(msg.width * 0.7)
            
            for row in range(start_row, end_row):
                for col in range(start_col, end_col):
                    idx = row * msg.width + col
                    data_start = idx * point_step
                    data_end = data_start + point_step
                    
                    if data_end <= len(msg.data):
                        # Извлекаем значение глубины
                        value_bytes = msg.data[data_start:data_end]
                        if len(value_bytes) == 4:
                            # Распаковываем float32
                            depth = struct.unpack('f', value_bytes)[0]
                            
                            # Игнорируем невалидные значения
                            if 0.1 < depth < self.stop_distance:
                                if depth < min_distance:
                                    min_distance = depth
            
            # Проверяем обнаружение препятствия
            if min_distance < float('inf'):
                if min_distance < self.stop_distance:
                    if not self.obstacle_detected:
                        self.obstacle_detected = True
                        self.get_logger().warn(f'ПРЕПЯТСТВИЕ! Дистанция: {min_distance:.2f} м')
                else:
                    if self.obstacle_detected:
                        self.obstacle_detected = False
                        self.get_logger().info('Путь свободен, продолжаем')
            
        except Exception as e:
            self.get_logger().error(f'Ошибка: {e}')
    
    def publish_cmd(self):
        """Публикация команды скорости"""
        cmd = Twist()
        
        if self.obstacle_detected:
            # СТОП
            cmd.linear.x = 0.0
            cmd.angular.z = 0.0
        else:
            # ДВИЖЕНИЕ ВПЕРЕД
            cmd.linear.x = self.forward_speed
            cmd.angular.z = 0.0
        
        self.cmd_pub.publish(cmd)

def main(args=None):
    rclpy.init(args=args)
    node = SimpleObstacleStop()
    
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        # Останавливаем робота
        stop_cmd = Twist()
        node.cmd_pub.publish(stop_cmd)
        node.get_logger().info('Остановка...')
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()