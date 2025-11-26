#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import math

class CircleMovement(Node):
    def __init__(self):
        super().__init__('circle_movement')
        
        self.cmd_vel_publisher = self.create_publisher(
            Twist, 
            '/diff_drive/cmd_vel', 
            10
        )
        
        self.declare_parameter('base_speed', 0.5)
        self.declare_parameter('amplitude', 0.3)
        self.declare_parameter('frequency', 0.5)
        
        self.base_speed = self.get_parameter('base_speed').value
        self.amplitude = self.get_parameter('amplitude').value
        self.frequency = self.get_parameter('frequency').value
        
        self.start_time = self.get_clock().now()
        self.phase_shift = 0.0
        
        self.timer = self.create_timer(0.1, self.timer_callback)
        
        self.get_logger().info('Cos wave movement node started')
        self.get_logger().info(f'Base speed: {self.base_speed} m/s')
        self.get_logger().info(f'Amplitude: {self.amplitude} rad/s')
        self.get_logger().info(f'Frequency: {self.frequency} Hz')
        self.get_logger().info('Robot will move in cosine wave pattern!')
        
    def timer_callback(self):
        twist_msg = Twist()
        
        # Расчет времени с начала работы
        current_time = self.get_clock().now()
        elapsed_time = (current_time - self.start_time).nanoseconds / 1e9
        
        # Косинусоидальное изменение угловой скорости
        # Робот будет плавно "вилять" по синусоидальной траектории
        angular_speed = self.amplitude * math.cos(2 * math.pi * self.frequency * elapsed_time + self.phase_shift)
        
        # Линейная скорость также может немного меняться для большего разнообразия
        linear_speed = self.base_speed + 0.1 * math.sin(2 * math.pi * self.frequency * 0.3 * elapsed_time)
        
        # Ограничиваем скорости для безопасности
        linear_speed = max(0.1, min(linear_speed, 0.8))
        angular_speed = max(-1.0, min(angular_speed, 1.0))
        
        twist_msg.linear.x = linear_speed
        twist_msg.angular.z = angular_speed
        
        self.cmd_vel_publisher.publish(twist_msg)
        
        # Логируем каждые 8 секунд
        if hasattr(self, 'last_log_time'):
            if (current_time - self.last_log_time).nanoseconds > 8e9:
                self.get_logger().info(
                    f'Publishing cmd_vel: linear.x={linear_speed:.2f}, '
                    f'angular.z={angular_speed:.2f}, time={elapsed_time:.1f}s'
                )
                self.last_log_time = current_time
        else:
            self.last_log_time = current_time
            
        # Каждые 20 секунд меняем фазу для разнообразия
        if elapsed_time > 20.0 and not hasattr(self, 'phase_changed'):
            self.phase_shift += math.pi / 2
            self.get_logger().info('Phase shift changed! New movement pattern.')
            self.phase_changed = True

def main(args=None):
    rclpy.init(args=args)
    
    circle_movement = CircleMovement()
    
    try:
        rclpy.spin(circle_movement)
    except KeyboardInterrupt:
        pass
    finally:
        stop_msg = Twist()
        circle_movement.cmd_vel_publisher.publish(stop_msg)
        circle_movement.get_logger().info('Stopping robot and shutting down...')
        circle_movement.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()