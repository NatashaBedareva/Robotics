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
        
        self.declare_parameter('linear_speed', 0.5)
        self.declare_parameter('angular_speed', 0.25)
        
        self.linear_speed = self.get_parameter('linear_speed').value
        self.angular_speed = self.get_parameter('angular_speed').value
  
        self.circle_radius = self.linear_speed / self.angular_speed
        
        self.timer = self.create_timer(0.1, self.timer_callback)
        
        self.get_logger().info('Circle movement node started')
        self.get_logger().info(f'Linear speed: {self.linear_speed} m/s')
        self.get_logger().info(f'Angular speed: {self.angular_speed} rad/s')
        self.get_logger().info(f'Circle radius: {self.circle_radius:.2f} m')
        
    def timer_callback(self):
        twist_msg = Twist()

        twist_msg.linear.x = self.linear_speed
        twist_msg.angular.z = self.angular_speed
        
        self.cmd_vel_publisher.publish(twist_msg)
        
        current_time = self.get_clock().now()
        if hasattr(self, 'last_log_time'):
            if (current_time - self.last_log_time).nanoseconds > 5e9:
                self.get_logger().info(
                    f'Publishing cmd_vel: linear.x={self.linear_speed}, '
                    f'angular.z={self.angular_speed}'
                )
                self.last_log_time = current_time
        else:
            self.last_log_time = current_time

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