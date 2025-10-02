from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess

def generate_launch_description():
    return LaunchDescription([
        
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='turtlesim1',
            output='screen',
            parameters=[{'background_r': 100, 'background_g': 100, 'background_b': 100}]
        ),
        
        
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='turtlesim2',
            output='screen',
            parameters=[{'background_r': 150, 'background_g': 150, 'background_b': 150}]
        ),
        
        
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='turtlesim3',
            output='screen'
        ),
        
        
        Node(
            package='turtlesim',
            executable='mimic',
            name='mimic1',
            output='screen',
            parameters=[{'target_frame': 'turtle1', 'mimic_frame': 'turtle2'}]
        ),
        
        
        Node(
            package='turtlesim',
            executable='mimic',
            name='mimic2',
            output='screen',
            parameters=[{'target_frame': 'turtle2', 'mimic_frame': 'turtle3'}]
        )
    ])
