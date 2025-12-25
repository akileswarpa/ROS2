import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64


class numbercounter(Node):

    def  __init__(self):
        super().__init__("numbercounter")
        self.subscriber = self.create_subscription(Int64,"number",self.callback_data,10)
        self.get_logger().info(("Started receiving data...."))

        self.publisher = self.create_publisher(Int64,"number_count",10)
        self.timer = self.create_timer(1, self.publisher_station)
        self.received_data = 0


    def callback_data(self, msg: Int64 ):
        self.get_logger().info("Received data : "+ str( msg.data))
        self.received_data = msg.data



    def  publisher_station(self):
        msg = Int64()
        msg.data = self.received_data
        self.publisher.publish(msg)
        self.get_logger().info("published Data :" + str(msg.data))


def main(args=None):
    rclpy.init(args=args)
    node = numbercounter()
    rclpy.spin(node)
    rclpy.shutdown()




if  "__init__" == "__main__":
    main()



