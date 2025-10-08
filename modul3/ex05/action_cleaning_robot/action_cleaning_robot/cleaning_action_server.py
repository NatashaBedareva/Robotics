#!/usr/bin/env python3

import rclpy
from rclpy.action import ActionServer
from rclpy.node import Node
import math
import time

from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from action_cleaning_robot.action import CleaningTask


class CleaningActionServer(Node):

    def __init__(self):
        super().__init__('cleaning_action_server')
        
        # Publishers and subscribers
        self.cmd_vel_publisher = self.create_publisher(Twist, 'cmd_vel', 10)
        self.pose_subscriber = self.create_subscription(Pose, 'pose', self.pose_callback, 10)
        
        # Action server
        self._action_server = ActionServer(
            self,
            CleaningTask,
            'CleaningTask',
            self.execute_callback)
        
        # Current pose
        self.current_pose = None
        self.start_pose = None
        
        # Cleaning parameters
        self.linear_speed = 1.0
        self.angular_speed = 1.0
        self.cleaning_resolution = 0.5  # meters between cleaning points
        
        self.get_logger().info('Cleaning Action Server started')

    def pose_callback(self, msg):
        self.current_pose = msg

    def wait_for_pose(self):
        while self.current_pose is None and rclpy.ok():
            self.get_logger().info('Waiting for pose information...')
            time.sleep(0.1)

    def move_to_point(self, target_x, target_y, tolerance=0.1):
        """Move turtle to specific point"""
        while self.current_pose is None:
            time.sleep(0.1)
            
        distance = math.sqrt((target_x - self.current_pose.x)**2 + 
                           (target_y - self.current_pose.y)**2)
        
        while distance > tolerance and rclpy.ok():
            # Calculate angle to target
            angle_to_target = math.atan2(target_y - self.current_pose.y, 
                                       target_x - self.current_pose.x)
            angle_diff = angle_to_target - self.current_pose.theta
            
            # Normalize angle difference
            while angle_diff > math.pi:
                angle_diff -= 2 * math.pi
            while angle_diff < -math.pi:
                angle_diff += 2 * math.pi
            
            # Create twist message
            twist = Twist()
            
            # Rotate towards target
            if abs(angle_diff) > 0.1:
                twist.angular.z = self.angular_speed * (1.0 if angle_diff > 0 else -1.0)
            else:
                # Move towards target
                twist.linear.x = self.linear_speed
                
            self.cmd_vel_publisher.publish(twist)
            time.sleep(0.1)
            
            # Update distance
            distance = math.sqrt((target_x - self.current_pose.x)**2 + 
                               (target_y - self.current_pose.y)**2)
        
        # Stop
        twist = Twist()
        self.cmd_vel_publisher.publish(twist)
        time.sleep(0.5)

    def clean_square(self, size, goal_handle):
        """Clean square area starting from current position"""
        if self.current_pose is None:
            return False, 0, 0.0
            
        self.start_pose = self.current_pose
        start_x, start_y = self.start_pose.x, self.start_pose.y
        
        # Calculate number of passes
        num_passes = int(size / self.cleaning_resolution)
        total_points = num_passes * num_passes
        cleaned_points = 0
        total_distance = 0.0
        
        self.get_logger().info(f'Cleaning square of size {size}m with {total_points} points')
        
        for i in range(num_passes):
            for j in range(num_passes):
                if goal_handle.is_cancel_requested:
                    goal_handle.canceled()
                    return False, cleaned_points, total_distance
                
                # Calculate target point
                target_x = start_x + j * self.cleaning_resolution
                target_y = start_y + i * self.cleaning_resolution
                
                # Move to point
                initial_x, initial_y = self.current_pose.x, self.current_pose.y
                self.move_to_point(target_x, target_y)
                
                # Calculate distance traveled
                distance = math.sqrt((self.current_pose.x - initial_x)**2 + 
                                   (self.current_pose.y - initial_y)**2)
                total_distance += distance
                
                cleaned_points += 1
                
                # Publish feedback
                feedback_msg = CleaningTask.Feedback()
                feedback_msg.progress_percent = int((cleaned_points / total_points) * 100)
                feedback_msg.current_cleaned_points = cleaned_points
                feedback_msg.current_x = self.current_pose.x
                feedback_msg.current_y = self.current_pose.y
                
                goal_handle.publish_feedback(feedback_msg)
                
                self.get_logger().info(f'Cleaned point {cleaned_points}/{total_points} '
                                     f'({feedback_msg.progress_percent}%)')
        
        return True, cleaned_points, total_distance

    def clean_circle(self, radius, goal_handle):
        """Clean circular area around current position"""
        if self.current_pose is None:
            return False, 0, 0.0
            
        center_x, center_y = self.current_pose.x, self.current_pose.y
        
        # Calculate number of points
        circumference = 2 * math.pi * radius
        num_points = int(circumference / self.cleaning_resolution)
        cleaned_points = 0
        total_distance = 0.0
        
        self.get_logger().info(f'Cleaning circle with radius {radius}m and {num_points} points')
        
        for i in range(num_points):
            if goal_handle.is_cancel_requested:
                goal_handle.canceled()
                return False, cleaned_points, total_distance
            
            # Calculate point on circle
            angle = 2 * math.pi * i / num_points
            target_x = center_x + radius * math.cos(angle)
            target_y = center_y + radius * math.sin(angle)
            
            # Move to point
            initial_x, initial_y = self.current_pose.x, self.current_pose.y
            self.move_to_point(target_x, target_y)
            
            # Calculate distance traveled
            distance = math.sqrt((self.current_pose.x - initial_x)**2 + 
                               (self.current_pose.y - initial_y)**2)
            total_distance += distance
            
            cleaned_points += 1
            
            # Publish feedback
            feedback_msg = CleaningTask.Feedback()
            feedback_msg.progress_percent = int((cleaned_points / num_points) * 100)
            feedback_msg.current_cleaned_points = cleaned_points
            feedback_msg.current_x = self.current_pose.x
            feedback_msg.current_y = self.current_pose.y
            
            goal_handle.publish_feedback(feedback_msg)
            
            self.get_logger().info(f'Cleaned point {cleaned_points}/{num_points} '
                                 f'({feedback_msg.progress_percent}%)')
        
        return True, cleaned_points, total_distance

    def return_home(self, target_x, target_y, goal_handle):
        """Return to home position"""
        self.get_logger().info(f'Returning home to ({target_x}, {target_y})')
        
        # Move to home position
        initial_x, initial_y = self.current_pose.x, self.current_pose.y
        self.move_to_point(target_x, target_y)
        
        # Calculate distance
        distance = math.sqrt((self.current_pose.x - initial_x)**2 + 
                           (self.current_pose.y - initial_y)**2)
        
        # Publish completion feedback
        feedback_msg = CleaningTask.Feedback()
        feedback_msg.progress_percent = 100
        feedback_msg.current_cleaned_points = 0
        feedback_msg.current_x = self.current_pose.x
        feedback_msg.current_y = self.current_pose.y
        goal_handle.publish_feedback(feedback_msg)
        
        return True, 0, distance

    def execute_callback(self, goal_handle):
        """Main action execution callback"""
        self.get_logger().info(f'Executing goal: {goal_handle.request.task_type}')
        
        # Wait for pose information
        self.wait_for_pose()
        
        success = False
        cleaned_points = 0
        total_distance = 0.0
        
        try:
            if goal_handle.request.task_type == 'clean_square':
                success, cleaned_points, total_distance = self.clean_square(
                    goal_handle.request.area_size, goal_handle)
                    
            elif goal_handle.request.task_type == 'clean_circle':
                success, cleaned_points, total_distance = self.clean_circle(
                    goal_handle.request.area_size, goal_handle)
                    
            elif goal_handle.request.task_type == 'return_home':
                success, cleaned_points, total_distance = self.return_home(
                    goal_handle.request.target_x, goal_handle.request.target_y, goal_handle)
            
            else:
                self.get_logger().error(f'Unknown task type: {goal_handle.request.task_type}')
                success = False
        
        except Exception as e:
            self.get_logger().error(f'Error executing task: {str(e)}')
            success = False
        
        # Set result
        result = CleaningTask.Result()
        result.success = success
        result.cleaned_points = cleaned_points
        result.total_distance = total_distance
        
        if success:
            goal_handle.succeed()
            self.get_logger().info('Task completed successfully')
        else:
            goal_handle.abort()
            self.get_logger().info('Task failed')
        
        return result


def main(args=None):
    rclpy.init(args=args)
    cleaning_action_server = CleaningActionServer()
    
    try:
        rclpy.spin(cleaning_action_server)
    except KeyboardInterrupt:
        pass
    finally:
        cleaning_action_server.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
