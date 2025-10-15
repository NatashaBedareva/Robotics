cmake_minimum_required(VERSION 3.8)
project(service_full_name)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(rosidl_default_generators REQUIRED)

# Генерируем интерфейсы из srv файла
rosidl_generate_interfaces(${PROJECT_NAME}
  "srv/SummFullName.srv"
)

# Устанавливаем Python скрипты КАК ИСПОЛНЯЕМЫЕ ФАЙЛЫ
install(PROGRAMS
  service_full_name/service_node.py
  service_full_name/client_node.py
  DESTINATION lib/${PROJECT_NAME}
)

# Устанавливаем srv файлы
install(
  DIRECTORY srv
  DESTINATION share/${PROJECT_NAME}
)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()