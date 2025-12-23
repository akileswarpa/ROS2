import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class autonomousCar(Node):          #create the class name
    def __init__(self):
        super().__init__("autonomousCar_Node")   # create the NODE
        
        self.subscriber = self.create_subscription(String,"lidar_data",self.callback_data,10)
    

    def callback_data(self, msg: String ):
        self.get_logger().info(" Received Data: "+ msg.data)


def main(args=None):
    rclpy.init(args=args)       #initiate the Rclpy library
    node = autonomousCar()
    rclpy.spin(node)
    rclpy.shutdown()


if "__init__" == "__main__":
    main()




    #**************SUBSCRIBER NODE******************#

