import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node
import sys
import uuid

from action_cleaning_robot.action import CleaningTask


class CleaningActionClient(Node):
    def __init__(self):
        super().__init__('cleaning_action_client')
        self._action_client = ActionClient(self, CleaningTask, 'cleaning_task')
        self.goal_handles = {}
        self.current_goal_id = None

    def send_goal(self, task_type, area_size=0.0, target_x=0.0, target_y=0.0):
        goal_msg = CleaningTask.Goal()
        goal_msg.task_type = task_type
        goal_msg.area_size = area_size
        goal_msg.target_x = target_x
        goal_msg.target_y = target_y

        self._action_client.wait_for_server()


        self._send_goal_future = self._action_client.send_goal_async(goal_msg, feedback_callback=self.feedback_callback)
        self.get_logger().info(f'Sending goal: {task_type}')
        self._send_goal_future.add_done_callback(self.goal_response_callback)
        

    def goal_response_callback(self, future):
        goal_handle = future.result()

        if not goal_handle.accepted:
            self.get_logger().info('Goal rejected :(')
            return

        self.get_logger().info('Goal accepted :)')

        self._get_result_future = goal_handle.get_result_async()
        self._get_result_future.add_done_callback(self.get_result_callback)

    def get_result_callback(self, future):
        goal_handle = future.result()

        #self.get_logger().info('Result: {0}'.format(result.sequence))
        self.get_logger().info("УРА ЧЕРЕПАХА ДОМА")
        
        self.get_logger().info('result tut')
        rclpy.shutdown()

    def feedback_callback(self, feedback_msg):
        feedback = feedback_msg.feedback
        self.get_logger().info("УРА ЧЕРЕПАХА ДОМА")
        self.get_logger().info("Процент выполнения: {0}%".format(feedback.progress_percent))
        self.get_logger().info("Зачищенных точек: {0}".format(feedback.current_cleaned_points))
    
 



def main(args=None):
    rclpy.init(args=args)

    action_client = CleaningActionClient()

    import sys

    if sys.argv[1]  == 'clean':
        action_client.send_goal("clean_square", area_size=3.0)
    elif sys.argv[1]  == 'home':
        action_client.send_goal("return_home", target_x=5.5, target_y=5.5)
    else:
        print('invalid')
    rclpy.spin(action_client)
    


if __name__ == '__main__':
    main()