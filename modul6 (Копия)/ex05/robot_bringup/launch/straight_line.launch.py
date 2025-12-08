import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, TimerAction
from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, Command
from launch_ros.parameter_descriptions import ParameterValue
from launch_ros.actions import Node

def generate_launch_description():
    # Пути к пакетам
    pkg_project_bringup = get_package_share_directory('robot_bringup')
    pkg_project_description = get_package_share_directory('robot_description')
    pkg_ros_gz_sim = get_package_share_directory('ros_gz_sim')

    urdf_path  =  os.path.join(pkg_project_description, 'urdf', 'robot.urdf.xacro')
    robot_desc = ParameterValue(Command(['xacro ', urdf_path]), value_type=str)

    # Запуск Gazebo симулятора
    gz_sim = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_ros_gz_sim, 'launch', 'gz_sim.launch.py')),
        launch_arguments={'gz_args': "-r empty.sdf"}.items(),
    )

    # Создание робота в симуляторе
    create = Node(
        package='ros_gz_sim',
        executable='create',
        arguments=['-name', 'robot',
                   '-topic', 'robot_description',
                   '-x', '0.0',
                   '-y', '0.0',
                   '-z', '0.1',
                ],
        output='screen',
    )

    # Публикатор состояния робота
    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='both',
        parameters=[
            {'robot_description': robot_desc},
            {'frame_prefix': "robot/"}
        ]
    )

    # RViz для визуализации
    rviz = Node(
       package='rviz2',
       executable='rviz2',
       arguments=['-d', os.path.join(pkg_project_bringup, 'config', 'diff_drive.rviz')],
       condition=IfCondition(LaunchConfiguration('rviz'))
    )


    bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        parameters=[{
            'config_file': os.path.join(pkg_project_bringup, 'config', 'robot_bridge.yaml'),
            'qos_overrides./tf_static.publisher.durability': 'transient_local',
        }],
        output='screen'
    )

    straight_line_node = Node(
        package='robot_bringup',
        executable='simple_stop', 
        name='simple_stop',
        output='screen',
        parameters=[{
            'stop_distance': 1.5,    
            'forward_speed': 0.3,      
        }]
    )

    return LaunchDescription([
        DeclareLaunchArgument('rviz', default_value='true',
                            description='Запустить RViz'),
        
        gz_sim,
        bridge,
        robot_state_publisher,
        rviz,

        TimerAction(
            period=3.0,
            actions=[create]),
        
        TimerAction(
            period=5.0,
            actions=[straight_line_node]),
    ])