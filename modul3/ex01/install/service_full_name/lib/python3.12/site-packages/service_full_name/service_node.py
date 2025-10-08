#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_srvs.srv import SetBool


class FullNameService(Node):

    def __init__(self):
        super().__init__('service_name')
        # Используем SetBool service, но будем передавать данные через глобальные переменные
        self.srv = self.create_service(
            SetBool, 
            'SummFullName', 
            self.combine_full_name_callback
        )
        self.get_logger().info('Full Name Service is ready...')
        # Храним данные для сервиса
        self.last_name = ""
        self.first_name = ""
        self.patronymic = ""

    def combine_full_name_callback(self, request, response):
        # Используем поле data для передачи признака того, что данные готовы
        if request.data:
            full_name = f"{self.last_name} {self.first_name} {self.patronymic}"
            response.success = True
            response.message = full_name
            self.get_logger().info(f'Sending full name: {full_name}')
            
            # Очищаем данные после отправки
            self.last_name = ""
            self.first_name = ""
            self.patronymic = ""
        else:
            response.success = False
            response.message = "Data not set"
            
        return response

    def set_name_data(self, last_name, first_name, patronymic):
        self.last_name = last_name
        self.first_name = first_name
        self.patronymic = patronymic
        self.get_logger().info(f'Name data set: {last_name}, {first_name}, {patronymic}')


def main(args=None):
    rclpy.init(args=args)
    full_name_service = FullNameService()
    try:
        rclpy.spin(full_name_service)
    except KeyboardInterrupt:
        pass
    finally:
        full_name_service.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
