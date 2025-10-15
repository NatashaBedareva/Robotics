from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # Окно 1
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='turtlesim1',
            output='screen',
            parameters=[{'background_r': 100, 'background_g': 100, 'background_b': 100}]
        ),
        
        # Окно 2
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='turtlesim2',
            output='screen',
            parameters=[{'background_r': 150, 'background_g': 150, 'background_b': 150}]
        ),
        
        # Окно 3
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='turtlesim3',
            output='screen',
            parameters=[{'background_r': 200, 'background_g': 200, 'background_b': 200}]
        ),
        
        
        Node(
            package='turtlesim',
            executable='mimic',
            name='mimic1',
            output='screen',
            remappings=[
                ('input/pose', 'turtle1/pose'),
                ('output/cmd_vel', 'turtle2/cmd_vel')
            ]
        ),
        
        
        Node(
            package='turtlesim',
            executable='mimic',
            name='mimic2',
            output='screen',
            remappings=[
                ('input/pose', 'turtle2/pose'),
                ('output/cmd_vel', 'turtle3/cmd_vel')
            ]
        )
    ])
