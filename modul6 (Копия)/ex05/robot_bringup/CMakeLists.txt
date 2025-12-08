cmake_minimum_required(VERSION 3.5)

project(robot_bringup)

find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(std_srvs REQUIRED)

# Установка Python скриптов
install(PROGRAMS
  scripts/simple_stop.py  # Изменили название здесь
  DESTINATION lib/${PROJECT_NAME}
)

# Установка launch файлов
install(
  DIRECTORY
    launch/
  DESTINATION share/${PROJECT_NAME}/launch
)

# Установка конфигурационных файлов
install(
  DIRECTORY
    config/
  DESTINATION share/${PROJECT_NAME}/config
)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()