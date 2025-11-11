from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument, ExecuteProcess
from launch.substitutions import LaunchConfiguration
import math

def generate_launch_description():
    return LaunchDescription([
        # Параметры
        DeclareLaunchArgument('radius1', default_value='2.0'),
        DeclareLaunchArgument('direction1', default_value='1'),
        DeclareLaunchArgument('radius2', default_value='1.5'), 
        DeclareLaunchArgument('direction2', default_value='-1'),
        DeclareLaunchArgument('switch_threshold', default_value='1.0'),

        # Turtlesim node
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='sim'
        ),

        # Спавнер черепашек (запускаем первым)
        Node(
            package='mycarrot',
            executable='turtle_spawner',
            name='turtle_spawner'
        ),

        # Broadcaster для turtle1
        Node(
            package='mycarrot',
            executable='turtle_tf2_broadcaster',
            name='broadcaster1',
            parameters=[{'turtlename': 'turtle1'}]
        ),

        # Broadcaster для turtle2
        Node(
            package='mycarrot', 
            executable='turtle_tf2_broadcaster',
            name='broadcaster2',
            parameters=[{'turtlename': 'turtle2'}]
        ),

        # Broadcaster для turtle3
        Node(
            package='mycarrot',
            executable='turtle_tf2_broadcaster', 
            name='broadcaster3',
            parameters=[{'turtlename': 'turtle3'}]
        ),

        # Carrot1 для turtle1
        Node(
            package='mycarrot',
            executable='carrot_tf2_broadcaster',
            name='carrot1_broadcaster',
            parameters=[
                {'turtlename': 'turtle1'},
                {'carrotname': 'carrot1'},
                {'radius': LaunchConfiguration('radius1')},
                {'direction': LaunchConfiguration('direction1')}
            ]
        ),

        # Carrot2 для turtle3
        Node(
            package='mycarrot',
            executable='carrot_tf2_broadcaster',
            name='carrot2_broadcaster', 
            parameters=[
                {'turtlename': 'turtle3'},
                {'carrotname': 'carrot2'},
                {'radius': LaunchConfiguration('radius2')},
                {'direction': LaunchConfiguration('direction2')}
            ]
        ),

        # Static target
        Node(
            package='mycarrot',
            executable='static_target_broadcaster',
            name='static_target_broadcaster'
        ),

        # Target switcher (добавляем задержку для инициализации TF)
        Node(
            package='mycarrot',
            executable='target_switcher',
            name='target_switcher',
            parameters=[{'switch_threshold': LaunchConfiguration('switch_threshold')}],
            # Задержка для инициализации TF дерева
            # arguments=['--ros-args', '--log-level', 'info']
        ),

        # Turtle controller (также с задержкой)
        Node(
            package='mycarrot',
            executable='turtle_controller',
            name='turtle_controller',
            # arguments=['--ros-args', '--log-level', 'info'] 
        )
    ])