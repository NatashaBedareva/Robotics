#!/usr/bin/env python3
import sys
import rclpy
from rclpy.node import Node
from service_full_name.srv import SummFullName

class ClientName(Node):
    def __init__(self):
        super().__init__('client_name')
        self.cli = self.create_client(SummFullName, 'SummFullName')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service not available, waiting again...')
        self.req = SummFullName.Request()

    def send_request(self, last_name, name, first_name):
        self.req.last_name = last_name
        self.req.name = name
        self.req.first_name = first_name
        self.future = self.cli.call_async(self.req)
        rclpy.spin_until_future_complete(self, self.future)
        return self.future.result()

def main(args=None):
    rclpy.init(args=args)
    
    if len(sys.argv) != 4:
        print("Usage: ros2 run service_full_name client_name <last_name> <name> <first_name>")
        return
    
    client = ClientName()
    response = client.send_request(sys.argv[1], sys.argv[2], sys.argv[3])
    
    if response is not None:
        client.get_logger().info(f'Full name: {response.full_name}')
    else:
        client.get_logger().error('Service call failed')
    
    client.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()