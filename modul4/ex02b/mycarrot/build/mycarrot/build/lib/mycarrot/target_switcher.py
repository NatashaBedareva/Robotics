import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from tf2_ros import TransformException, Buffer, TransformListener
import math

class TargetSwitcher(Node):
    def __init__(self):
        super().__init__('target_switcher')
        
        # Параметры
        self.switch_threshold = self.declare_parameter(
            'switch_threshold', 1.0).get_parameter_value().double_value
        
        # Список целей и текущая цель
        self.targets = ['carrot1', 'carrot2', 'static_target']
        self.current_target_index = 0
        self.current_target = self.targets[self.current_target_index]
        
        # TF
        self.tf_buffer = Buffer()
        self.tf_listener = TransformListener(self.tf_buffer, self)
        
        # Publisher для текущей цели
        self.target_pub = self.create_publisher(String, '/current_target', 10)
        
        # Таймер для автоматического переключения
        self.timer = self.create_timer(0.1, self.check_target_distance)
        
        # Подписка на клавиатуру для ручного переключения
        self.key_sub = self.create_subscription(
            String,
            '/keyboard_input',
            self.handle_keyboard_input,
            10
        )
        
        self.get_logger().info(f'Target switcher started. Initial target: {self.current_target}')
    
    def handle_keyboard_input(self, msg):
        if msg.data == 'n':
            self.switch_to_next_target()
    
    def switch_to_next_target(self):
        self.current_target_index = (self.current_target_index + 1) % len(self.targets)
        self.current_target = self.targets[self.current_target_index]
        
        # Публикуем новую цель
        target_msg = String()
        target_msg.data = self.current_target
        self.target_pub.publish(target_msg)
        
        self.get_logger().info(f'Switched to target: {self.current_target}')
    
    def check_target_distance(self):
        try:
            # Получаем трансформацию между turtle2 и текущей целью
            t = self.tf_buffer.lookup_transform(
                'turtle2',
                self.current_target,
                rclpy.time.Time()
            )
            
            # Вычисляем расстояние
            distance = math.sqrt(
                t.transform.translation.x ** 2 +
                t.transform.translation.y ** 2
            )
            
            # Автоматическое переключение при достижении порога
            if distance < self.switch_threshold:
                self.switch_to_next_target()
                
        except TransformException as ex:
            self.get_logger().debug(f'Could not transform: {ex}')
    
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