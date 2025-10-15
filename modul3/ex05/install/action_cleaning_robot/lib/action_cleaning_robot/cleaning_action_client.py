#!/usr/bin/env python3
import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node
import sys
import time

from action_cleaning_robot.action import CleaningTask

class CleaningActionClient(Node):
    def __init__(self):
        super().__init__('cleaning_action_client')
        self._action_client = ActionClient(self, CleaningTask, 'CleaningTask')
        self.get_logger().info('Cleaning Action Client started')
        self.current_goal_handle = None
    
    def send_goal(self, task_type, area_size=0.0, target_x=0.0, target_y=0.0):
        """Отправка цели действию"""
        goal_msg = CleaningTask.Goal()
        goal_msg.task_type = task_type
        goal_msg.area_size = area_size
        goal_msg.target_x = target_x
        goal_msg.target_y = target_y
        
        self.get_logger().info(f'Waiting for action server...')
        self._action_client.wait_for_server()
        
        self.get_logger().info(f'Sending goal: {task_type}')
        
        self._send_goal_future = self._action_client.send_goal_async(
            goal_msg,
            feedback_callback=self.feedback_callback
        )
        
        self._send_goal_future.add_done_callback(self.goal_response_callback)
        
        return self._send_goal_future
    
    def goal_response_callback(self, future):
        """Обработчик ответа на цель"""
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info('Goal rejected :(')
            return
            
        self.get_logger().info('Goal accepted :)')
        self.current_goal_handle = goal_handle
        
        self._get_result_future = goal_handle.get_result_async()
        self._get_result_future.add_done_callback(self.get_result_callback)
    
    def get_result_callback(self, future):
        """Обработчик результата"""
        result = future.result().result
        self.get_logger().info(f'Result: Success={result.success}, '
                              f'Cleaned Points={result.cleaned_points}, '
                              f'Total Distance={result.total_distance:.2f}m')
        
        # Сигнализируем о завершении задачи
        self.task_completed = True
    
    def feedback_callback(self, feedback_msg):
        """Обработчик feedback"""
        feedback = feedback_msg.feedback
        self.get_logger().info(f'Feedback: Progress={feedback.progress_percent}%, '
                              f'Points={feedback.current_cleaned_points}, '
                              f'Position=({feedback.current_x:.2f}, {feedback.current_y:.2f})')

def execute_task_sequence(action_client):
    """Выполнение последовательности задач"""
    tasks = [
        # Сначала убираем квадратную область 2x2 метра
        {"task_type": "clean_square", "area_size": 2.0},
        
        # Возвращаемся домой
        {"task_type": "return_home", "target_x": 5.5, "target_y": 5.5}
    ]
    
    for i, task in enumerate(tasks):
        action_client.get_logger().info(f'Executing task {i + 1}: {task["task_type"]}')
        
        # Сбрасываем флаг завершения
        action_client.task_completed = False
        
        if task["task_type"] == "return_home":
            action_client.send_goal(
                task["task_type"],
                target_x=task["target_x"],
                target_y=task["target_y"]
            )
        else:
            action_client.send_goal(
                task["task_type"],
                area_size=task["area_size"]
            )
        
        # Ждем завершения текущей задачи
        while not action_client.task_completed:
            rclpy.spin_once(action_client, timeout_sec=0.1)
        
        action_client.get_logger().info(f'Task {i + 1} completed. Waiting 2 seconds...')
        time.sleep(2)  # Пауза между задачами

def main(args=None):
    rclpy.init(args=args)
    
    action_client = CleaningActionClient()
    
    try:
        # Выполняем последовательность задач
        execute_task_sequence(action_client)
        
        action_client.get_logger().info('All tasks completed!')
        
    except KeyboardInterrupt:
        action_client.get_logger().info('Client interrupted')
    except Exception as e:
        action_client.get_logger().error(f'Error: {e}')
    finally:
        action_client.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()