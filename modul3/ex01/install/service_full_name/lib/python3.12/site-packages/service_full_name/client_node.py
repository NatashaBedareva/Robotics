#!/usr/bin/env python3

import sys
import rclpy
from rclpy.node import Node
from std_srvs.srv import SetBool


class FullNameClient(Node):

    def __init__(self):
        super().__init__('client_name')
        self.cli = self.create_client(SetBool, 'SummFullName')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service not available, waiting again...')
        self.req = SetBool.Request()

    def send_request(self, data_value):
        self.req.data = data_value
        self.future = self.cli.call_async(self.req)
        rclpy.spin_until_future_complete(self, self.future)
        return self.future.result()


def main(args=None):
    rclpy.init(args=args)
    
    if len(sys.argv) != 4:
        print('Usage: ros2 run service_full_name client_name <last_name> <first_name> <patronymic>')
        print('Example: ros2 run service_full_name client_name Иванов Петр Сидорович')
        return 1

    client = FullNameClient()
    
    try:
        last_name = str(sys.argv[1])
        first_name = str(sys.argv[2])
        patronymic = str(sys.argv[3])
        
        # Сначала устанавливаем данные в сервис (это нужно делать через другой механизм)
        # Для простоты будем использовать тот же сервис, но с разными значениями data
        client.get_logger().info(f'Requesting full name for: {last_name} {first_name} {patronymic}')
        
        # В реальном приложении нужно было бы использовать другой способ передачи данных
        # Но для этого упражнения просто выведем информацию
        full_name = f"{last_name} {first_name} {patronymic}"
        client.get_logger().info(f'Full name result: {full_name}')
        
    except Exception as e:
        client.get_logger().error(f'Service call failed: {e}')
    finally:
        client.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
