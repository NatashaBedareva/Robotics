import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer
from rclpy.action.server import ServerGoalHandle
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose 
import math
import time

from action_cleaning_robot.action import CleaningTask


class CleaningActionServer(Node):
    def __init__(self):
        super().__init__('cleaning_action_server')
        
        # Action сервер
        self._action_server = ActionServer(
            self,
            CleaningTask,
            'cleaning_task',
            self.execute_callback
        )
        
        self.home_x = 5.5
        self.home_y = 5.5
        self.current_pose = None
        self.is_moving = False
        self.cleaned_points = 0
        self.total_distance = 0.0
        self.last_position = None
        

        self.cmd_vel_publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.pose_subscriber = self.create_subscription(
            Pose, 
            '/turtle1/pose', 
            self.pose_callback, 
            10
        )
 
        self.linear_kp = 1.5
        self.angular_kp = 6.0
        self.distance_tolerance = 0.1
        self.angle_tolerance = 0.05
        
        self.get_logger().info('Cleaning Action Server started')
            
    def pose_callback(self, msg):
        self.current_pose = msg
            
    def execute_callback(self, goal_handle: ServerGoalHandle):
        self.get_logger().info(f'Executing goal: {goal_handle.request.task_type}')
        
        goal = goal_handle.request
        result = CleaningTask.Result()
    
        self.cleaned_points = 0
        self.total_distance = 0.0
        
        try:
            if goal.task_type == "clean_square":
                success = self.clean_square(goal_handle, goal.area_size)
            elif goal.task_type == "return_home":
                success = self.return_home(goal_handle)

                
            result.success = success
            result.cleaned_points = self.cleaned_points
            result.total_distance = self.total_distance
            
            if success:
                goal_handle.succeed()
                self.get_logger().info('Task completed successfully')
            else:
                goal_handle.abort()
                self.get_logger().info('Task failed')
                
        except Exception as e:
            self.get_logger().error(f'Error during task execution: {str(e)}')
            result.success = False
            goal_handle.abort()
            
        return result

    def move_to_coord(self, target_x, target_y):
        """Движение к координате: сначала поворот, потом движение по прямой"""
        if self.current_pose is None:
            self.get_logger().error('No pose data available')
            return False
            
        self.get_logger().info(f'Moving to: ({target_x:.2f}, {target_y:.2f}) from ({self.current_pose.x:.2f}, {self.current_pose.y:.2f})')
        
        # ФАЗА 1: ПОВОРОТ К ЦЕЛИ
        self.get_logger().info('PHASE 1: Rotating to target')
        
        max_rotation_iterations = 200
        rotation_iteration = 0
        
        while rotation_iteration < max_rotation_iterations:

            rclpy.spin_once(self,timeout_sec = 0.01)

            if self.current_pose is None:
                return False
                
            # Вычисляем целевой угол
            dx = target_x - self.current_pose.x
            dy = target_y - self.current_pose.y
            target_angle = math.atan2(dy, dx) 
            angle_error = self.normalize_angle(target_angle - self.current_pose.theta)
            
            # Если правильно повернулись, выходим из фазы поворота
            if abs(angle_error) < 0.05:  # ~3 градуса
                twist = Twist()
                self.cmd_vel_publisher.publish(twist)
                self.get_logger().info('Rotation completed!')
                break
                
            # Поворачиваемся
            twist = Twist()
            twist.angular.z = 2.0 * angle_error
            twist.angular.z = max(min(twist.angular.z, 2.0), -2.0)
            
            self.cmd_vel_publisher.publish(twist)
            rotation_iteration += 1
            time.sleep(0.1)  # ИСПРАВЛЕНО: было 5 секунд, теперь 0.1
            
            if rotation_iteration % 20 == 0:
                self.get_logger().info(f'Rotation progress: angle_error={angle_error:.3f}')
                self.get_logger().info(f'Rotation progress: angle_current={self.current_pose.theta:.3f}')
        
        if rotation_iteration >= max_rotation_iterations:
            self.get_logger().warn('Rotation timeout')
            twist = Twist()
            self.cmd_vel_publisher.publish(twist)
            return False
        
        # Небольшая пауза после поворота
        time.sleep(0.5)
            
            # ФАЗА 2: ДВИЖЕНИЕ ПО ПРЯМОЙ
        self.get_logger().info('PHASE 2: Moving straight to target')

        max_movement_iterations = 300
        movement_iteration = 0

        while movement_iteration < max_movement_iterations:

            rclpy.spin_once(self,timeout_sec = 0.01)


            if self.current_pose is None:
                return False
                    
            dx = target_x - self.current_pose.x
            dy = target_y - self.current_pose.y
            distance_error = math.sqrt(dx**2 + dy**2)
                
            if distance_error < self.distance_tolerance:
                twist = Twist()
                self.cmd_vel_publisher.publish(twist)
                self.get_logger().info('Target reached!')
                return True
                    
            twist = Twist()
            twist.linear.x = 0.5 
            twist.angular.z = 0.0  
                
            self.cmd_vel_publisher.publish(twist)
            movement_iteration += 1
            time.sleep(0.1)
                
            if movement_iteration % 10 == 0:
                self.get_logger().info(f'Movement: dist={distance_error:.3f}, pos=({self.current_pose.x:.2f}, {self.current_pose.y:.2f}), theta={math.degrees(self.current_pose.theta):.1f}°')

    
        twist = Twist()
        self.cmd_vel_publisher.publish(twist)
        self.get_logger().warn('Movement timeout')
        return False

    def normalize_angle(self, angle):
        """Нормализуем угол в диапазон [-pi, pi]"""
        while angle > math.pi:
            angle -= 2.0 * math.pi
        while angle < -math.pi:
            angle += 2.0 * math.pi
        return angle
    
    def distance_error(self,x,y):
        dx = x - self.current_pose.x
        dy = y - self.current_pose.y
        dist_error = math.sqrt(dx**2 + dy**2)
        return dist_error


    def clean_square(self, goal_handle, area_size=3.0):
        """Очистка квадратной области"""
        if self.current_pose is None:
            return False
        

        right_low_x = self.current_pose.x + area_size
        right_low_y = self.current_pose.y 

        left_low_x = self.current_pose.x
        left_low_y = self.current_pose.y

        right_high_x = self.current_pose.x + area_size
        right_high_y = self.current_pose.y + area_size

        left_high_x = self.current_pose.x
        left_high_y = self.current_pose.y + area_size

        # создаём точки по границе левой и правой

        points_left = [(left_high_x,left_high_y)] 
        step = area_size/10
        
        i = left_high_y
        while i>left_low_y:
            i-=step
            points_left.append((left_high_x,i))

        points_right = [(right_high_x,right_high_y)] 
        
        i = right_high_y
        while i>right_low_y:
            i-=step
            points_right.append((right_high_x,i))

        print(points_right)
        print(points_left)



        dist_error = self.distance_error(right_high_x,right_high_y)
        
        
        not self.move_to_coord(right_high_x,right_high_y)

        all_points = len(points_left)
        self.cleaned_points = 0

        def step_feedback():
            rclpy.spin_once(self,timeout_sec = 0.01)
            feedback = CleaningTask.Feedback()
            feedback.progress_percent = int( (self.cleaned_points * 100 ) // all_points)
            feedback.current_cleaned_points = self.cleaned_points
            feedback.current_x = self.current_pose.x
            feedback.current_y = self.current_pose.y
            goal_handle.publish_feedback(feedback)


        in_right = True
        for i in range(len(points_left)):
            self.cleaned_points+=1
            if in_right:
                self.move_to_coord(points_left[i][0],points_left[i][1])
                step_feedback()
                in_right=False
            else:
                self.move_to_coord(points_right[i][0],points_right[i][1])
                step_feedback()
                in_right=True
   
        return True
        

    def return_home(self, goal_handle):
        rclpy.spin_once(self,timeout_sec = 0.01)
        
        
        success = self.move_to_coord(self.home_x, self.home_y)
        

        if success:
            feedback = CleaningTask.Feedback()
            feedback.progress_percent = int( 100)
            feedback.current_cleaned_points = self.cleaned_points
            feedback.current_x = self.current_pose.x
            feedback.current_y = self.current_pose.y
            goal_handle.publish_feedback(feedback)
            
        return success


def main(args=None):
    rclpy.init(args=args)
    action_server = CleaningActionServer()
    
    try:
        rclpy.spin(action_server)
    except KeyboardInterrupt:
        pass
    finally:
        action_server.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()