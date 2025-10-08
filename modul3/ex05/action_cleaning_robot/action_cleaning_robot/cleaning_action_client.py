#!/usr/bin/env python3

import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node
import time

from action_cleaning_robot.action import CleaningTask


class CleaningActionClient(Node):

    def __init__(self):
        super().__init__('cleaning_action_client')
        self._action_client = ActionClient(self, CleaningTask, 'CleaningTask')
        self.get_logger().info('Cleaning Action Client started')

    def wait_for_server(self):
        self.get_logger().info('Waiting for action server...')
        return self._action_client.wait_for_server()

    def send_goal(self, task_type, area_size=0.0, target_x=0.0, target_y=0.0):
        goal_msg = CleaningTask.Goal()
        goal_msg.task_type = task_type
        goal_msg.area_size = area_size
        goal_msg.target_x = target_x
        goal_msg.target_y = target_y
        
        self.get_logger().info(f'Sending goal: {task_type}')
        
        self._action_client.wait_for_server()
        return self._action_client.send_goal_async(
            goal_msg,
            feedback_callback=self.feedback_callback)

    def feedback_callback(self, feedback_msg):
        feedback = feedback_msg.feedback
        self.get_logger().info(
            f'Feedback: {feedback.progress_percent}% complete, '
            f'cleaned {feedback.current_cleaned_points} points, '
            f'position: ({feedback.current_x:.2f}, {feedback.current_y:.2f})'
        )


def main(args=None):
    rclpy.init(args=args)
    
    client = CleaningActionClient()
    client.wait_for_server()
    
    # Execute cleaning sequence
    future_goals = []
    
    # Clean 3x3 meter square
    future_goals.append(client.send_goal('clean_square', 3.0))
    
    # Clean circle with radius 2 meters
    future_goals.append(client.send_goal('clean_circle', 2.0))
    
    # Return home
    future_goals.append(client.send_goal('return_home', target_x=5.5, target_y=5.5))
    
    # Wait for all goals to complete
    for i, future_goal in enumerate(future_goals):
        rclpy.spin_until_future_complete(client, future_goal)
        goal_handle = future_goal.result()
        
        if not goal_handle.accepted:
            client.get_logger().error(f'Goal {i+1} was rejected!')
            continue
            
        client.get_logger().info(f'Goal {i+1} accepted')
        
        # Wait for result
        future_result = goal_handle.get_result_async()
        rclpy.spin_until_future_complete(client, future_result)
        
        result = future_result.result().result
        if result.success:
            client.get_logger().info(
                f'Goal {i+1} completed: {result.cleaned_points} points cleaned, '
                f'distance: {result.total_distance:.2f}m'
            )
        else:
            client.get_logger().error(f'Goal {i+1} failed!')
    
    client.get_logger().info('All cleaning tasks completed!')
    client.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
