import rclpy
from rclpy.node import Node
from turtlesim.srv import Spawn
import time

class TurtleSpawner(Node):
    def __init__(self):
        super().__init__('turtle_spawner')
        

        self.spawn_client = self.create_client(Spawn, 'spawn')
        
        while not self.spawn_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Spawn service not available, waiting...')
        

        self.spawn_turtle('turtle2', 4.0, 2.0, 0.0)
        time.sleep(1)
        
        self.spawn_turtle('turtle3', 8.0, 8.0, 0.0)
        
        self.get_logger().info('All turtles spawned successfully')
    
    def spawn_turtle(self, name, x, y, theta):
        request = Spawn.Request()
        request.name = name
        request.x = x
        request.y = y
        request.theta = theta
        
        future = self.spawn_client.call_async(request)
        rclpy.spin_until_future_complete(self, future)
        
        if future.result() is not None:
            self.get_logger().info(f'Spawned {name} at ({x}, {y})')
        else:
            self.get_logger().error(f'Failed to spawn {name}')

def main():
    rclpy.init()
    node = TurtleSpawner()

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()