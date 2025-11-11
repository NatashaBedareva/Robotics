import math
from geometry_msgs.msg import Twist, TransformStamped
from std_msgs.msg import String
import rclpy
from rclpy.node import Node
from tf2_ros import TransformException, Buffer, TransformListener

class TurtleController(Node):
    def __init__(self):
        super().__init__('turtle_controller')
        
        # Текущая цель
        self.current_target = 'carrot1'
        
        # TF
        self.tf_buffer = Buffer()
        self.tf_listener = TransformListener(self.tf_buffer, self)
        
        # Publisher для управления turtle2
        self.cmd_vel_pub = self.create_publisher(Twist, 'turtle2/cmd_vel', 10)
        
        # Publisher для информации о текущей цели
        self.target_info_pub = self.create_publisher(String, '/current_target_info', 10)
        
        # Подписка на смену целей
        self.target_sub = self.create_subscription(
            String,
            '/current_target',
            self.handle_target_change,
            10
        )
        
        # Таймер для управления
        self.timer = self.create_timer(0.1, self.control_loop)
        
        self.get_logger().info('Turtle controller started')
    
    def handle_target_change(self, msg):
        self.current_target = msg.data
        self.get_logger().info(f'New target received: {self.current_target}')
        
        # Публикуем информацию о цели
        info_msg = String()
        info_msg.data = f'Turtle2 is following: {self.current_target}'
        self.target_info_pub.publish(info_msg)
    
    def control_loop(self):
        try:
            # Получаем трансформацию между turtle2 и текущей целью
            t = self.tf_buffer.lookup_transform(
                'turtle2',
                self.current_target,
                rclpy.time.Time()
            )
            
            # Создаем сообщение управления
            msg = Twist()
            
            # Угловая скорость (поворот к цели)
            scale_rotation_rate = 2.0
            msg.angular.z = scale_rotation_rate * math.atan2(
                t.transform.translation.y,
                t.transform.translation.x
            )
            
            # Линейная скорость (движение к цели)
            scale_forward_speed = 0.8
            distance = math.sqrt(
                t.transform.translation.x ** 2 +
                t.transform.translation.y ** 2
            )
            
            # Замедляемся при приближении к цели
            if distance < 1.0:
                msg.linear.x = scale_forward_speed * distance * 0.5
            else:
                msg.linear.x = scale_forward_speed * distance
            
            # Ограничиваем максимальную скорость
            msg.linear.x = min(msg.linear.x, 2.0)
            
            self.cmd_vel_pub.publish(msg)
            
        except TransformException as ex:
            self.get_logger().debug(f'Could not transform: {ex}')

def main():
    rclpy.init()
    node = TurtleController()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    rclpy.shutdown()