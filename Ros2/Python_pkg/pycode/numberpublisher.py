import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64

class numberpublisher(Node):
    def __init__(self):
        super().__init__("numberpublisher")
        self.publisher = self.create_publisher(Int64,"number",10)
        self.timer = self.create_timer(1,self.publisher_station)
        self.get_logger().info("Number start publishing....")
        self.count = 0


    def publisher_station(self):
        msg = Int64()
        self.count  = self.count + 1
        msg.data = self.count
        self.publisher.publish(msg)
        self.get_logger().info("Publish Number :"+str(msg.data))


def main(args=None):
    rclpy.init(args=args)
    node = numberpublisher()
    rclpy.spin(node)
    rclpy.shutdown()



if "__init__"== "__main__":
    main()