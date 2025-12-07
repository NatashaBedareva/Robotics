import os
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    
    obstacle_avoidance_node = Node(
        package='robot_bringup',
        executable='depth_obstacle_avoidance',
        name='depth_obstacle_avoidance',
        output='screen',
        parameters=[{
            'obstacle_distance': 1.0,  # метры
            'min_height': 0.1,         # минимальная высота препятствия
            'max_height': 0.5,         # максимальная высота препятствия
            'center_region': 0.3,      # центральная область (30% ширины)
            'stop_timeout': 2.0,       # секунды ожидания
        }]
    )
    
    return LaunchDescription([
        obstacle_avoidance_node,
    ])