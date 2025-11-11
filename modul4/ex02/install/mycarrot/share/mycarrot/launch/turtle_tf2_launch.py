
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='sim'
        ),
        Node(
            package='mycarrot',
            executable='turtle_tf2_broadcaster',
            name='broadcaster1',
            parameters=[
                {'turtlename': 'turtle1'}
            ]
        ),
        DeclareLaunchArgument(
            'target_frame', default_value='carrot',
            description='Target frame name.'
        ),
        Node(
            package='mycarrot',
            executable='turtle_tf2_broadcaster',
            name='broadcaster2',
            parameters=[
                {'turtlename': 'turtle2'}
            ]
        ),
        Node(
            package='mycarrot',
            executable='carrot_tf2_broadcaster',
            name='broadcaster3',
            parameters=[
                {'turtlename': 'turtle1'}
            ]
        ),
        Node(
            package='mycarrot',
            executable='turtle_tf2_listener',
            name='listener',
            parameters=[
                {'target_frame': LaunchConfiguration('target_frame')}
            ]
        ),
        Node(
            package='mycarrot',
            executable='turtle3_tf2_listener',
            name='listener3',
            parameters=[
                {'target_frame': LaunchConfiguration('target_frame')}
            ]
        )

    ])