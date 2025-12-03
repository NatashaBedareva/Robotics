#!/usr/bin/env python3
"""
Управление роботом с лидаром для автоматического движения с остановкой перед препятствиями.
Стек: ROS 2 Jazzy, Gazebo Harmonic
"""

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
import math

class ObstacleAvoidance(Node):
    def __init__(self):
        super().__init__('obstacle_avoidance_node')
        
        # Параметры управления
        self.linear_speed = 0.5  # м/с - скорость движения вперед
        self.angular_speed = 0.0  # рад/с - скорость поворота
        self.stop_distance = 1.0  # м - дистанция для остановки
        self.slowdown_distance = 2.0  # м - дистанция для начала замедления
        self.resume_delay = 1.0  # с - задержка перед возобновлением движения
        self.scan_width = 30  # градусы - ширина сектора сканирования спереди
        
        # Состояние робота
        self.obstacle_detected = False
        self.last_obstacle_time = None
        self.current_speed = 0.0
        self.running = True
        
        # Издатель команд движения - ИЗМЕНЕНО имя топика
        self.cmd_vel_publisher = self.create_publisher(
            Twist,
            '/diff_drive/cmd_vel',  # ИЗМЕНЕНО: было '/model/diff_drive/cmd_vel'
            10
        )
        
        # Подписчик на данные лидара - ИЗМЕНЕНО имя топика
        self.laser_subscriber = self.create_subscription(
            LaserScan,
            '/diff_drive/scan',  # ИЗМЕНЕНО: было '/lidar/scan'
            self.laser_callback,
            10
        )
        
        # Таймер для управления движением
        self.timer = self.create_timer(0.1, self.control_loop)  # 10 Гц
        
        self.get_logger().info('Obstacle avoidance node запущен')
        self.get_logger().info(f'Стоп-дистанция: {self.stop_distance} м')
        self.get_logger().info(f'Скорость движения: {self.linear_speed} м/с')
    
    def laser_callback(self, msg):
        """
        Обработка данных лидара.
        Обнаружение препятствий в переднем секторе.
        """
        if not msg.ranges:
            return
        
        # Определяем индексы для переднего сектора
        num_readings = len(msg.ranges)
        if num_readings == 0:
            return
            
        center_index = num_readings // 2
        half_width = int((self.scan_width / 2) * num_readings / 360)
        
        # Начинаем и заканчиваем индексы для сканирования
        start_idx = max(0, center_index - half_width)
        end_idx = min(num_readings, center_index + half_width)
        
        # Ищем минимальное расстояние в переднем секторе
        min_distance = float('inf')
        valid_distances = []
        
        for i in range(start_idx, end_idx):
            distance = msg.ranges[i]
            # Игнорируем некорректные значения
            if (math.isfinite(distance) and 
                distance >= msg.range_min and 
                distance <= msg.range_max and
                distance > 0):
                valid_distances.append(distance)
                if distance < min_distance:
                    min_distance = distance
        
        if not valid_distances:
            self.obstacle_detected = False
            return
        
        # Определяем, есть ли препятствие
        obstacle_in_range = min_distance <= self.slowdown_distance
        
        if obstacle_in_range:
            if not self.obstacle_detected:
                self.get_logger().info(f'Обнаружено препятствие на расстоянии: {min_distance:.2f} м')
                self.obstacle_detected = True
                self.last_obstacle_time = self.get_clock().now()
        else:
            if self.obstacle_detected:
                self.get_logger().info('Препятствие исчезло, готов к движению')
                self.obstacle_detected = False
    
    def control_loop(self):
        """
        Основной цикл управления движением робота.
        """
        if not self.running:
            return
            
        try:
            msg = Twist()
            
            if self.obstacle_detected:
                # Полная остановка, если препятствие слишком близко
                msg.linear.x = 0.0
                msg.angular.z = 0.0
                self.current_speed = 0.0
            else:
                # Плавное возобновление движения
                if self.current_speed < self.linear_speed:
                    self.current_speed += 0.1  # Плавное ускорение
                    if self.current_speed > self.linear_speed:
                        self.current_speed = self.linear_speed
                else:
                    self.current_speed = self.linear_speed
                
                msg.linear.x = self.current_speed
                msg.angular.z = 0.0  # Двигаемся прямо
            
            # Публикуем команду
            self.cmd_vel_publisher.publish(msg)
            
        except Exception as e:
            self.get_logger().error(f'Ошибка в control_loop: {str(e)}')
    
    def stop_robot(self):
        """Безопасная остановка робота."""
        self.running = False
        try:
            stop_msg = Twist()
            stop_msg.linear.x = 0.0
            stop_msg.angular.z = 0.0
            self.cmd_vel_publisher.publish(stop_msg)
            self.get_logger().info('Робот остановлен')
        except:
            pass  # Игнорируем ошибки при завершении


def main(args=None):
    rclpy.init(args=args)
    
    obstacle_avoidance = None
    
    try:
        obstacle_avoidance = ObstacleAvoidance()
        rclpy.spin(obstacle_avoidance)
    except KeyboardInterrupt:
        obstacle_avoidance.get_logger().info('Получен сигнал прерывания...')
    except Exception as e:
        obstacle_avoidance.get_logger().error(f'Ошибка: {str(e)}')
    finally:
        # Остановка робота при завершении
        if obstacle_avoidance:
            obstacle_avoidance.stop_robot()
            obstacle_avoidance.destroy_node()
        rclpy.try_shutdown()


if __name__ == '__main__':
    main()