cmake_minimum_required(VERSION 3.5)

project(ros_gz_example_bringup)

find_package(ament_cmake REQUIRED)
find_package(ros_gz_example_description REQUIRED)
find_package(ros_gz_example_gazebo REQUIRED)

# Установить Python скрипт как исполняемый файл
install(PROGRAMS
  scripts/obstacle_avoidance_node.py
  DESTINATION lib/${PROJECT_NAME}
)

# Установить launch файлы
install(
  DIRECTORY
    launch/
  DESTINATION share/${PROJECT_NAME}/launch
)

# Установить конфигурационные файлы
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