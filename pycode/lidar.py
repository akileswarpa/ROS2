#! /usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.msg import String


class lidar(Node):

    def __init__(self):
        super().__init__("Lidar_Node")    #create the node

        self.get_logger().info("Lidar")

        self.publisher= self.create_publisher(String,"lidar_data",10)   #Publish the topic with name lidar signal

        self.timer = self.create_timer(1, self.publisher_station)

        self.get_logger().info("Started_Data_Sending to Autonomous CAR: ")


    def publisher_station(self):
    
        msg = String()
        msg.data = "Hi, I am Lidar" 
        self.publisher.publish(msg)



def main(args=None):

    rclpy.init(args=args)

    node = lidar()

    rclpy.spin(node)

    rclpy.shutdown()


if "__init__" == "__main__":
    main()



#******************PUBLISHER NODE******************#












