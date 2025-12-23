#! /usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.msg import String


class robot_station_control(Node):

    def __init__(self):
        super().__init__("Robot_station")
        self.get_logger().info("Robot_station_print")

        self.publisher= self.create_publisher(String,"robot_signal",10)

        self.timer = self.create_timer(1, self.publisher_station)
        self.get_logger().info("Station_started")

    def publisher_station(self):
    
        msg = String()
        msg.data = "Station_1" 
        self.publisher.publish(msg)



def main(args=None):

    rclpy.init(args=args)

    node = robot_station_control()

    rclpy.spin(node)

    rclpy.shutdown()


if "__init__" == "__main__":
    main()













