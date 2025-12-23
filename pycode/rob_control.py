import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class robcontrol(Node):          #create the class name
    def __init__(self):
        super().__init__("PDI_control")   # create the NODE
        #self.subscriber = self.create_subscription(String,"robot_signal",self.callback_data,10)
        self.subscriber = self.create_subscription(String,"dis_data",self.callback_data,10)
    

    def callback_data(self, msg: String ):
        self.get_logger().info("I received data from robot "+ msg.data)


def main(args=None):
    rclpy.init(args=args)       #initiate the Rclpy library
    node = robcontrol()
    rclpy.spin(node)
    rclpy.shutdown()


if "__init__" == "__main__":
    main()

