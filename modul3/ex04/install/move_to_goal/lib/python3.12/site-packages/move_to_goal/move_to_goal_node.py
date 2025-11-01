#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim_msgs.msg import Pose 
import math
import sys

class MoveToGoal(Node):
    def __init__(self, target_x, target_y, target_theta):
        super().__init__('move_to_goal')
        
        self.target_x = target_x
        self.target_y = target_y 
        self.target_theta = target_theta
        self.current_pose = None
        
        # Публикатор для управления скоростью
        self.cmd_vel_publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        
        # Подписчик на позицию черепахи
        self.pose_subscriber = self.create_subscription(
            Pose, 
            '/turtle1/pose', 
            self.pose_callback, 
            10
        )
        
     
        self.control_timer = self.create_timer(0.1, self.control_loop)
        
        self.get_logger().info(f'Moving to goal: ({target_x}, {target_y}, {target_theta})')
        
        
        self.linear_kp = 1.5
        self.angular_kp = 6.0
        self.distance_tolerance = 0.1
        self.angle_tolerance = 0.05
        
    def pose_callback(self, msg):
        """Сохраняем текущую позицию черепахи"""
        self.current_pose = msg
        
    def control_loop(self):
        """Основной цикл управления"""
        if self.current_pose is None:
            return
            
       
        dx = self.target_x - self.current_pose.x
        dy = self.target_y - self.current_pose.y
        distance_error = math.sqrt(dx**2 + dy**2)
        
       
        target_angle = math.atan2(dy, dx)
        
      
        angle_error = self.normalize_angle(target_angle - self.current_pose.theta)
        
        
        twist = Twist()
        
       
        if distance_error < self.distance_tolerance:
            
            final_angle_error = self.normalize_angle(self.target_theta - self.current_pose.theta)
            
            if abs(final_angle_error) > self.angle_tolerance:
                twist.angular.z = self.angular_kp * final_angle_error
                self.get_logger().info(f'Rotating to target angle. Error: {final_angle_error:.3f}')
            else:
                twist.angular.z = 0.0
                self.get_logger().info('Goal reached!')
                self.control_timer.cancel()
        else:
            
            twist.linear.x = self.linear_kp * distance_error
            twist.angular.z = self.angular_kp * angle_error
            
          
            twist.linear.x = min(twist.linear.x, 2.0)
            twist.angular.z = max(min(twist.angular.z, 2.0), -2.0)
            
            self.get_logger().info(f'Moving to goal. Distance: {distance_error:.3f}, Angle: {angle_error:.3f}')
        
      
        self.cmd_vel_publisher.publish(twist)
        
    def normalize_angle(self, angle):
        """Нормализуем угол в диапазон [-pi, pi]"""
        while angle > math.pi:
            angle -= 2.0 * math.pi
        while angle < -math.pi:
            angle += 2.0 * math.pi
        return angle

def main(args=None):
    rclpy.init(args=args)
    
    if len(sys.argv) != 4:
        print("Usage: ros2 run move_to_goal move_to_goal_node <x> <y> <theta>")
        print("Example: ros2 run move_to_goal move_to_goal_node 5.0 5.0 0.0")
        return
    
    try:
        target_x = float(sys.argv[1])
        target_y = float(sys.argv[2]) 
        target_theta = float(sys.argv[3])
        
        if not (0 <= target_x <= 11 and 0 <= target_y <= 11):
            print("Error: Coordinates must be between 0 and 11")
            return
            
        node = MoveToGoal(target_x, target_y, target_theta)
        rclpy.spin(node)
        
    except ValueError:
        print("Error: All parameters must be numbers")
    except KeyboardInterrupt:
        pass
    finally:
        rclpy.shutdown()

if __name__ == '__main__':
    main()