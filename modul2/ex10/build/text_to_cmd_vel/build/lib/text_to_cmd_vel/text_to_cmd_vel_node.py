#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from geometry_msgs.msg import Twist

class TextToCmdVel(Node):
    def __init__(self):
        super().__init__('text_to_cmd_vel')
        
        # Подписка на текстовые команды
        self.subscription = self.create_subscription(
            String,
            'cmd_text',
            self.cmd_text_callback,
            10
        )
        
        # Публикация команд скорости
        self.publisher = self.create_publisher(
            Twist,
            '/turtle1/cmd_vel',
            10
        )
        
        self.get_logger().info('text_to_cmd_vel node started')
        self.get_logger().info('Available commands: "turn_right", "turn_left", "move_forward", "move_backward"')
    
    def cmd_text_callback(self, msg):
        command = msg.data.lower().strip()
        twist_msg = Twist()
        
        if command == "turn_right":
            # Поворот направо
            twist_msg.angular.z = -1.5  # радиан/сек
            self.get_logger().info(f'Command received: {command} - Turning right')
            
        elif command == "turn_left":
            # Поворот налево
            twist_msg.angular.z = 1.5   # радиан/сек
            self.get_logger().info(f'Command received: {command} - Turning left')
            
        elif command == "move_forward":
            # Движение вперед
            twist_msg.linear.x = 1.0    # метр/сек
            self.get_logger().info(f'Command received: {command} - Moving forward')
            
        elif command == "move_backward":
            # Движение назад
            twist_msg.linear.x = -1.0   # метр/сек
            self.get_logger().info(f'Command received: {command} - Moving backward')
            
        else:
            self.get_logger().warn(f'Unknown command: {command}')
            return
        
        # Публикация команды скорости
        self.publisher.publish(twist_msg)

def main(args=None):
    rclpy.init(args=args)
    node = TextToCmdVel()
    
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
