from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='ros_gz_example_bringup',
            executable='circle_movement.py',
            name='circle_movement',
            output='screen',
            parameters=[{
                'linear_speed': 0.5,
                'angular_speed': 0.25,
            }]
        ),
    ])