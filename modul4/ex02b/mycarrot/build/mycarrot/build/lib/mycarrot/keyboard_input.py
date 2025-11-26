import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import termios
import tty
import sys
import select

class KeyboardInput(Node):
    def __init__(self):
        super().__init__('keyboard_input')
        self.publisher = self.create_publisher(String, '/keyboard_input', 10)
        self.get_logger().info('Keyboard input node started. Press "n" to switch target, "q" to quit')
        
    def run(self):
        old_attr = termios.tcgetattr(sys.stdin)
        try:
            tty.setraw(sys.stdin.fileno())
            self.get_logger().info('Keyboard listener active. Press keys now...')
            while rclpy.ok():
                if select.select([sys.stdin], [], [], 0.1)[0]:
                    key = sys.stdin.read(1)
                    if key == 'n':
                        msg = String()
                        msg.data = 'n'
                        self.publisher.publish(msg)
                        self.get_logger().info('Target switch command sent')
                    elif key == 'q':
                        self.get_logger().info('Quitting...')
                        break
                    else:
                        self.get_logger().info(f'Pressed: {key} (only "n" and "q" work)')
        except Exception as e:
            self.get_logger().error(f'Error: {e}')
        finally:
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_attr)

def main():
    rclpy.init()
    node = KeyboardInput()
    try:
        node.run()
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()