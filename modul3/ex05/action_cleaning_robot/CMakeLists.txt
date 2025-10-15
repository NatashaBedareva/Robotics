cmake_minimum_required(VERSION 3.8)
project(action_cleaning_robot)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(ament_cmake_python REQUIRED)
find_package(rclpy REQUIRED)
find_package(rosidl_default_generators REQUIRED)

# Генерируем интерфейсы из action файла - ПРАВИЛЬНЫЙ СИНТАКСИС
rosidl_generate_interfaces(${PROJECT_NAME}
  "action/CleaningTask.action"
)

# Устанавливаем Python скрипты КАК ИСПОЛНЯЕМЫЕ ФАЙЛЫ
install(PROGRAMS
  action_cleaning_robot/cleaning_action_server.py
  action_cleaning_robot/cleaning_action_client.py
  DESTINATION lib/${PROJECT_NAME}
)

# Устанавливаем action файлы
install(
  DIRECTORY action
  DESTINATION share/${PROJECT_NAME}
)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()