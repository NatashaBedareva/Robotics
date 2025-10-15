#!/usr/bin/env python3
import rclpy
from rclpy.action import ActionServer
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim_msgs.msg import Pose
import math
import time

from action_cleaning_robot.action import CleaningTask

class CleaningActionServer(Node):
    def __init__(self):
        super().__init__('cleaning_action_server')
        
        # Action Server
        self._action_server = ActionServer(
            self,
            CleaningTask,
            'CleaningTask',
            self.execute_callback
        )
        
        # Публикатор для управления скоростью
        self.cmd_vel_publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        
        # Подписчик на позицию черепахи
        self.current_pose = None
        self.pose_subscriber = self.create_subscription(
            Pose,
            '/turtle1/pose',
            self.pose_callback,
            10
        )
        
        self.get_logger().info('Cleaning Action Server started')
        
        # Параметры управления
        self.linear_kp = 1.5
        self.angular_kp = 6.0
        
    def pose_callback(self, msg):
        """Сохраняем текущую позицию черепахи"""
        self.current_pose = msg
        
    def execute_callback(self, goal_handle):
        """Обработчик выполнения действия"""
        self.get_logger().info(f'Executing goal: {goal_handle.request.task_type}')
        
        feedback_msg = CleaningTask.Feedback()
        result = CleaningTask.Result()
        
        task_type = goal_handle.request.task_type
        area_size = goal_handle.request.area_size
        
        if task_type == "clean_square":
            success, cleaned_points, total_distance = self.clean_square(goal_handle, feedback_msg, area_size)
        elif task_type == "clean_circle":
            success, cleaned_points, total_distance = self.clean_circle(goal_handle, feedback_msg, area_size)
        elif task_type == "return_home":
            success, cleaned_points, total_distance = self.return_home(
                goal_handle, feedback_msg, 
                goal_handle.request.target_x, goal_handle.request.target_y
            )
        else:
            self.get_logger().error(f'Unknown task type: {task_type}')
            result.success = False
            result.cleaned_points = 0
            result.total_distance = 0.0
            goal_handle.abort()
            return result
        
        result.success = success
        result.cleaned_points = cleaned_points
        result.total_distance = total_distance
        
        if success:
            goal_handle.succeed()
        else:
            goal_handle.abort()
            
        return result
    
    def clean_square(self, goal_handle, feedback_msg, size):
        """Уборка квадратной области"""
        self.get_logger().info(f'Cleaning square area: {size}x{size} meters')
        
        if self.current_pose is None:
            self.get_logger().error('No pose information available')
            return False, 0, 0.0
        
        start_x = self.current_pose.x
        start_y = self.current_pose.y
        total_points = int(size * 10)  # Упрощенная модель - 10 точек на метр
        cleaned_points = 0
        total_distance = 0.0
        
        # Простой алгоритм движения по квадратной спирали
        for i in range(total_points):
            if goal_handle.is_cancel_requested:
                self.get_logger().info('Goal canceled')
                return False, cleaned_points, total_distance
                
            # Вычисляем следующую точку в спирали
            t = i / total_points * 4 * math.pi
            r = (size / 2) * (t / (4 * math.pi))
            target_x = start_x + r * math.cos(t)
            target_y = start_y + r * math.sin(t)
            
            # Двигаемся к точке
            distance = self.move_to_point(target_x, target_y, 0.0)
            total_distance += distance
            
            cleaned_points += 1
            
            # Отправляем feedback
            feedback_msg.progress_percent = int((i + 1) / total_points * 100)
            feedback_msg.current_cleaned_points = cleaned_points
            feedback_msg.current_x = self.current_pose.x
            feedback_msg.current_y = self.current_pose.y
            goal_handle.publish_feedback(feedback_msg)
            
            time.sleep(0.1)  # Небольшая задержка для имитации уборки
            
        self.stop_robot()
        return True, cleaned_points, total_distance
    
    def clean_circle(self, goal_handle, feedback_msg, radius):
        """Уборка круглой области"""
        self.get_logger().info(f'Cleaning circular area with radius: {radius} meters')
        
        if self.current_pose is None:
            self.get_logger().error('No pose information available')
            return False, 0, 0.0
        
        center_x = self.current_pose.x
        center_y = self.current_pose.y
        total_points = int(2 * math.pi * radius * 5)  # 5 точек на метр окружности
        cleaned_points = 0
        total_distance = 0.0
        
        # Движение по кругу
        for i in range(total_points):
            if goal_handle.is_cancel_requested:
                self.get_logger().info('Goal canceled')
                return False, cleaned_points, total_distance
                
            angle = 2 * math.pi * i / total_points
            target_x = center_x + radius * math.cos(angle)
            target_y = center_y + radius * math.sin(angle)
            target_theta = angle + math.pi/2  # Касательная к окружности
            
            distance = self.move_to_point(target_x, target_y, target_theta)
            total_distance += distance
            
            cleaned_points += 1
            
            # Отправляем feedback
            feedback_msg.progress_percent = int((i + 1) / total_points * 100)
            feedback_msg.current_cleaned_points = cleaned_points
            feedback_msg.current_x = self.current_pose.x
            feedback_msg.current_y = self.current_pose.y
            goal_handle.publish_feedback(feedback_msg)
            
            time.sleep(0.05)
            
        self.stop_robot()
        return True, cleaned_points, total_distance
    
    def return_home(self, goal_handle, feedback_msg, home_x, home_y):
        """Возвращение домой"""
        self.get_logger().info(f'Returning home to: ({home_x}, {home_y})')
        
        if self.current_pose is None:
            self.get_logger().error('No pose information available')
            return False, 0, 0.0
        
        # Просто движемся к целевой точке
        total_distance = self.move_to_point(home_x, home_y, 0.0)
        
        # Отправляем feedback
        feedback_msg.progress_percent = 100
        feedback_msg.current_cleaned_points = 0
        feedback_msg.current_x = self.current_pose.x
        feedback_msg.current_y = self.current_pose.y
        goal_handle.publish_feedback(feedback_msg)
        
        self.stop_robot()
        return True, 0, total_distance
    
    def move_to_point(self, target_x, target_y, target_theta, timeout=30):
        """Движение к целевой точке"""
        start_time = time.time()
        distance_traveled = 0.0
        last_x = self.current_pose.x
        last_y = self.current_pose.y
        
        while time.time() - start_time < timeout:
            if self.current_pose is None:
                continue
                
            # Вычисляем ошибку позиции
            dx = target_x - self.current_pose.x
            dy = target_y - self.current_pose.y
            distance_error = math.sqrt(dx**2 + dy**2)
            
            # Вычисляем пройденное расстояние
            distance_traveled += math.sqrt(
                (self.current_pose.x - last_x)**2 + 
                (self.current_pose.y - last_y)**2
            )
            last_x = self.current_pose.x
            last_y = self.current_pose.y
            
            if distance_error < 0.1:  # Достигли цели
                break
                
            # Вычисляем целевой угол
            target_angle = math.atan2(dy, dx)
            angle_error = self.normalize_angle(target_angle - self.current_pose.theta)
            
            # Публикуем команду скорости
            twist = Twist()
            twist.linear.x = min(self.linear_kp * distance_error, 2.0)
            twist.angular.z = max(min(self.angular_kp * angle_error, 2.0), -2.0)
            self.cmd_vel_publisher.publish(twist)
            
            time.sleep(0.1)
            
        self.stop_robot()
        return distance_traveled
    
    def stop_robot(self):
        """Остановка робота"""
        twist = Twist()
        twist.linear.x = 0.0
        twist.angular.z = 0.0
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