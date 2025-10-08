#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import math
import sys
import time

class MoveToGoal(Node):
    def __init__(self, goal_x, goal_y, goal_theta):
        super().__init__('move_to_goal')
        
        # Goal coordinates from command line
        self.goal_x = goal_x
        self.goal_y = goal_y 
        self.goal_theta = goal_theta
        
        # Estimated turtle pose (we'll estimate based on cmd_vel commands)
        self.estimated_x = 5.5  # Default turtlesim start position
        self.estimated_y = 5.5
        self.estimated_theta = 0.0
        
        # Control parameters
        self.linear_tolerance = 0.1
        self.angular_tolerance = 0.05
        self.max_linear_speed = 1.5
        self.max_angular_speed = 1.5
        self.linear_kp = 1.2
        self.angular_kp = 3.0
        
        # State variables
        self.goal_reached = False
        self.last_control_time = time.time()
        self.phase = "ROTATE_TO_GOAL"  # ROTATE_TO_GOAL, MOVE_TO_GOAL, ROTATE_TO_TARGET
        
        # Publishers - ONLY using cmd_vel as required
        self.cmd_vel_publisher = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        
        # Control timer - main loop
        self.control_timer = self.create_timer(0.1, self.control_loop)
        
        self.get_logger().info(f'MoveToGoal initialized. Target: ({goal_x:.2f}, {goal_y:.2f}, {goal_theta:.2f})')
        self.get_logger().info('Using internal pose estimation')
        
    def update_pose_estimate(self, linear_vel, angular_vel, dt):
        """Update estimated pose based on velocity commands (simple odometry)"""
        # Update orientation first
        self.estimated_theta += angular_vel * dt
        
        # Normalize angle to [-pi, pi]
        self.estimated_theta = self.normalize_angle(self.estimated_theta)
            
        # Update position based on current orientation
        self.estimated_x += linear_vel * math.cos(self.estimated_theta) * dt
        self.estimated_y += linear_vel * math.sin(self.estimated_theta) * dt
        
        # Keep within turtlesim bounds (optional)
        self.estimated_x = max(0.0, min(11.0, self.estimated_x))
        self.estimated_y = max(0.0, min(11.0, self.estimated_y))
        
    def normalize_angle(self, angle):
        """Normalize angle to [-pi, pi] range"""
        while angle > math.pi:
            angle -= 2.0 * math.pi
        while angle < -math.pi:
            angle += 2.0 * math.pi
        return angle
        
    def control_loop(self):
        """Main control loop - uses ONLY cmd_vel for control"""
        if self.goal_reached:
            return
            
        current_time = time.time()
        dt = current_time - self.last_control_time
        self.last_control_time = current_time
        
        # Calculate position error
        dx = self.goal_x - self.estimated_x
        dy = self.goal_y - self.estimated_y
        distance_to_goal = math.sqrt(dx*dx + dy*dy)
        
        # Calculate desired heading towards goal position
        target_heading = math.atan2(dy, dx)
        heading_error = self.normalize_angle(target_heading - self.estimated_theta)
        
        # Final orientation error
        final_orientation_error = self.normalize_angle(self.goal_theta - self.estimated_theta)
        
        cmd_vel = Twist()
        
        # Three-phase navigation
        if self.phase == "ROTATE_TO_GOAL":
            # Phase 1: Rotate to face the goal position
            if abs(heading_error) > self.angular_tolerance:
                cmd_vel.angular.z = self.angular_kp * heading_error
                cmd_vel.angular.z = max(min(cmd_vel.angular.z, self.max_angular_speed), -self.max_angular_speed)
                self.get_logger().info(f'Phase 1 - Rotating to goal: error={heading_error:.3f}')
            else:
                self.phase = "MOVE_TO_GOAL"
                self.get_logger().info('Phase 1 complete - Starting movement to goal')
                
        elif self.phase == "MOVE_TO_GOAL":
            # Phase 2: Move towards goal while maintaining direction
            if distance_to_goal > self.linear_tolerance:
                # Move forward
                linear_speed = min(self.linear_kp * distance_to_goal, self.max_linear_speed)
                cmd_vel.linear.x = linear_speed
                
                # Small correction to maintain heading towards goal
                current_heading_error = self.normalize_angle(target_heading - self.estimated_theta)
                cmd_vel.angular.z = 0.8 * current_heading_error
                
                self.get_logger().info(f'Phase 2 - Moving: dist={distance_to_goal:.3f}')
            else:
                self.phase = "ROTATE_TO_TARGET"
                self.get_logger().info('Phase 2 complete - Starting final orientation')
                
        elif self.phase == "ROTATE_TO_TARGET":
            # Phase 3: Adjust to final target orientation
            if abs(final_orientation_error) > self.angular_tolerance:
                cmd_vel.angular.z = self.angular_kp * final_orientation_error
                cmd_vel.angular.z = max(min(cmd_vel.angular.z, self.max_angular_speed), -self.max_angular_speed)
                self.get_logger().info(f'Phase 3 - Final orientation: error={final_orientation_error:.3f}')
            else:
                # Goal reached!
                cmd_vel.linear.x = 0.0
                cmd_vel.angular.z = 0.0
                self.cmd_vel_publisher.publish(cmd_vel)
                self.get_logger().info('🎯 Goal reached! '
                                      f'Position: ({self.estimated_x:.2f}, {self.estimated_y:.2f}), '
                                      f'Orientation: {self.estimated_theta:.2f}')
                self.goal_reached = True
                self.control_timer.cancel()
                rclpy.shutdown()
                return
        
        # Update pose estimate based on this command
        self.update_pose_estimate(cmd_vel.linear.x, cmd_vel.angular.z, dt)
        
        # Publish velocity command
        self.cmd_vel_publisher.publish(cmd_vel)

def main():
    if len(sys.argv) != 4:
        print("Usage: ros2 run move_to_goal move_to_goal <x> <y> <theta>")
        print("Example: ros2 run move_to_goal move_to_goal 5.0 5.0 0.0")
        return 1
        
    try:
        goal_x = float(sys.argv[1])
        goal_y = float(sys.argv[2])
        goal_theta = float(sys.argv[3])
    except ValueError:
        print("Error: All parameters must be numbers")
        return 1
        
    print(f"Starting MoveToGoal node...")
    print(f"Target: position=({goal_x:.2f}, {goal_y:.2f}), orientation={goal_theta:.2f}")
    
    rclpy.init()
    move_to_goal_node = MoveToGoal(goal_x, goal_y, goal_theta)
    
    try:
        rclpy.spin(move_to_goal_node)
    except KeyboardInterrupt:
        print("\nNode interrupted by user")
    finally:
        move_to_goal_node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()
        print("MoveToGoal node finished")
    
    return 0

if __name__ == '__main__':
    main()
