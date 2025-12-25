cmake_minimum_required(VERSION 3.8)
project(cpp_pkg)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(example_interfaces REQUIRED)


add_executable(Dis_sensor_extable src/distance_sensor.cpp)
ament_target_dependencies(Dis_sensor_extable rclcpp example_interfaces)

add_executable(control_extable src/control.cpp)
ament_target_dependencies(control_extable rclcpp example_interfaces)

add_executable(numberpublisher src/numberpublisher.cpp)
ament_target_dependencies(numberpublisher rclcpp example_interfaces)

add_executable(number_counter src/number_counter.cpp)
ament_target_dependencies(number_counter rclcpp example_interfaces)


install(TARGETS

   Dis_sensor_extable
   control_extable
   number_counter
   numberpublisher
   DESTINATION lib/${PROJECT_NAME}

)

ament_package()
