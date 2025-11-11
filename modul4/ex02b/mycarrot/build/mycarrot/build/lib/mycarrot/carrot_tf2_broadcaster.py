import math
from geometry_msgs.msg import TransformStamped
import numpy as np
import rclpy
from rclpy.node import Node
from tf2_ros import TransformBroadcaster
from turtlesim.msg import Pose

def quaternion_from_euler(ai, aj, ak):
    ai /= 2.0
    aj /= 2.0
    ak /= 2.0
    ci = math.cos(ai)
    si = math.sin(ai)
    cj = math.cos(aj)
    sj = math.sin(aj)
    ck = math.cos(ak)
    sk = math.sin(ak)
    cc = ci*ck
    cs = ci*sk
    sc = si*ck
    ss = si*sk

    q = np.empty((4, ))
    q[0] = cj*sc - sj*cs
    q[1] = cj*ss + sj*cc
    q[2] = cj*cs - sj*sc
    q[3] = cj*cc + sj*ss
    return q

class FramePublisher(Node):
    def __init__(self):
        super().__init__('carrot_tf2_broadcaster')

        # Параметры
        self.turtlename = self.declare_parameter(
            'turtlename', 'turtle1').get_parameter_value().string_value
        
        self.carrotname = self.declare_parameter(
            'carrotname', 'carrot1').get_parameter_value().string_value
            
        self.radius = self.declare_parameter(
            'radius', 2.0).get_parameter_value().double_value
            
        self.direction = self.declare_parameter(
            'direction', 1).get_parameter_value().integer_value

        # TF broadcaster
        self.tf_broadcaster = TransformBroadcaster(self)

        # Подписка на позицию черепахи
        self.subscription = self.create_subscription(
            Pose,
            f'/{self.turtlename}/pose',
            self.handle_turtle_pose,
            1
        )
        
        # Время начала
        self.start_time = self.get_clock().now()

    def handle_turtle_pose(self, msg):
        t = TransformStamped()

        t.header.stamp = self.get_clock().now().to_msg()
        t.header.frame_id = self.turtlename 
        t.child_frame_id = self.carrotname

        # Вычисляем позицию carrot на окружности
        now = self.get_clock().now()
        seconds = (now - self.start_time).nanoseconds / 1e9
        angular_speed = 0.5
        angle = self.direction * angular_speed * seconds
        
        t.transform.translation.x = self.radius * math.cos(angle)
        t.transform.translation.y = self.radius * math.sin(angle)
        t.transform.translation.z = 0.0
        
        q = quaternion_from_euler(0, 0, 0)
        t.transform.rotation.x = q[0]
        t.transform.rotation.y = q[1]
        t.transform.rotation.z = q[2]
        t.transform.rotation.w = q[3]

        self.tf_broadcaster.sendTransform(t)

def main():
    rclpy.init()
    node = FramePublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    rclpy.shutdown()