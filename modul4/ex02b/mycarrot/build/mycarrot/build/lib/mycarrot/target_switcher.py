import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from tf2_ros import TransformException, Buffer, TransformListener
import math

class TargetSwitcher(Node):
    def __init__(self):
        super().__init__('target_switcher')
        
        self.targets = ['carrot1', 'carrot2', 'static_target']
        self.current_target_index = 0
        self.current_target = self.targets[self.current_target_index]
        
        self.tf_buffer = Buffer()
        self.tf_listener = TransformListener(self.tf_buffer, self)
        
        self.target_pub = self.create_publisher(String, '/current_target', 10)
        
        self.publish_current_target()
        
        self.key_sub = self.create_subscription(
            String,
            '/keyboard_input',
            self.handle_keyboard_input,
            10
        )
        
        self.get_logger().info(f'Target switcher started. Initial target: {self.current_target}')

    def publish_current_target(self):
        target_msg = String()
        target_msg.data = self.current_target
        self.target_pub.publish(target_msg)
        self.get_logger().info(f'Published target: {self.current_target}')

    def handle_keyboard_input(self, msg):
        if msg.data == 'n':
            self.switch_to_next_target()
    
    def switch_to_next_target(self):
        self.current_target_index = (self.current_target_index + 1) % len(self.targets)
        self.current_target = self.targets[self.current_target_index]
        
        self.publish_current_target()
        self.get_logger().info(f'Switched to target: {self.current_target}')
    
    def get_current_target(self):
        return self.current_target

def main():
    rclpy.init()
    node = TargetSwitcher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    rclpy.shutdown()