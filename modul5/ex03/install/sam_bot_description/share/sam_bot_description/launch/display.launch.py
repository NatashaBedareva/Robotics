from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.conditions import IfCondition, UnlessCondition
from launch.substitutions import Command, LaunchConfiguration, PathJoinSubstitution
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
import os


def generate_launch_description():
    # Находим пакеты
    pkg_share = FindPackageShare(package='sam_bot_description').find('sam_bot_description')
    pkg_ros_gz_sim = FindPackageShare(package='ros_gz_sim').find('ros_gz_sim')
    
    # Пути к файлам
    default_model_path = os.path.join(pkg_share, 'src', 'description', 'sam_bot_description.xacro')
    default_rviz_config_path = os.path.join(pkg_share, 'rviz', 'config.rviz')
    bridge_config_path = os.path.join(pkg_share, 'config', 'ros_gz_bridge.yaml')
    
    # Аргументы запуска
    gui_arg = DeclareLaunchArgument(
        name='gui', 
        default_value='False',
        description='Flag to enable joint_state_publisher_gui'
    )
    
    model_arg = DeclareLaunchArgument(
        name='model', 
        default_value=default_model_path,
        description='Absolute path to robot XACRO file'
    )
    
    rviz_arg = DeclareLaunchArgument(
        name='rvizconfig', 
        default_value=default_rviz_config_path,
        description='Absolute path to rviz config file'
    )
    
    rviz_enable_arg = DeclareLaunchArgument(
        name='rviz',
        default_value='true',
        description='Enable RViz2'
    )

    # 1. Запуск симулятора Gazebo с ПУСТЫМ миром
    gz_sim = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_ros_gz_sim, 'launch', 'gz_sim.launch.py')),
        launch_arguments={
            'gz_args': '-r'  # Просто пустой мир без указания файла
        }.items(),
    )

    # 2. Публикатор состояния робота
    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='both',
        parameters=[{
            'use_sim_time': True,
            'robot_description': Command(['xacro ', LaunchConfiguration('model')])
        }]
    )

    # 3. Публикаторы состояния соединений
    joint_state_publisher_node = Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
        name='joint_state_publisher',
        condition=UnlessCondition(LaunchConfiguration('gui'))
    )

    joint_state_publisher_gui_node = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        name='joint_state_publisher_gui',
        condition=IfCondition(LaunchConfiguration('gui'))
    )

    # 4. RViz узел
    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        arguments=['-d', LaunchConfiguration('rvizconfig')],
        condition=IfCondition(LaunchConfiguration('rviz')),
        parameters=[{'use_sim_time': True}]
    )

    # 5. Мост между ROS и Gazebo
    bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        name='ros_gz_bridge',
        parameters=[{
            'config_file': bridge_config_path,
            'qos_overrides./tf_static.publisher.durability': 'transient_local',
        }],
        output='screen'
    )

    # 6. Спавн робота в симуляции
    spawn_entity = Node(
        package='ros_gz_sim',
        executable='create',
        arguments=[
            '-topic', '/robot_description',
            '-name', 'sam_bot',
            '-allow_renaming', 'true',
            '-x', '0.0',
            '-y', '0.0', 
            '-z', '0.5'  # Увеличим высоту чтобы не упал
        ],
        output='screen'
    )

    return LaunchDescription([
        # Аргументы
        gui_arg,
        model_arg,
        rviz_arg,
        rviz_enable_arg,
        
        # Узлы в правильном порядке
        gz_sim,
        robot_state_publisher_node,
        joint_state_publisher_node,
        joint_state_publisher_gui_node,
        bridge,
        spawn_entity,
        rviz_node
    ])