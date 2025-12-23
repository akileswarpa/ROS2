#! /usr/bin/env python3
import rclpy

from rclpy.node import Node


class tempnode(Node):
    
    def __init__(self):
        super().__init__("pynode")
        self.get_logger().info("pycoder")
        self.create_timer(1,self.time_call_back)


    def  time_call_back(self):
        self.get_logger().info("justprint")







def main(args=None):
    
    rclpy.init(args=args)
    # node= Node("pyNode")

    node = tempnode()


    node.get_logger().info("printpy")
    rclpy.spin(node)




    rclpy.shutdown()


if "__init__" == "__main__":
    main()