#include "rclcpp/rclcpp.hpp"
#include "example_interfaces/msg/int64.hpp"

using namespace std::chrono_literals;



class numberpublisher: public rclcpp::Node
{   
    int count = 0;

    public:
           numberpublisher(): Node("numberpublisher")
           {
                 
                 publisher_ = this->create_publisher<example_interfaces::msg::Int64>("number", 10 );
                 timer_ = this->create_wall_timer(1s,std::bind(&numberpublisher::publishdata,this));

                 RCLCPP_INFO(get_logger(),"Data start publishing.....");

           }
  

    private:
           
           void publishdata()
           {
            auto msg= example_interfaces::msg::Int64();
            count = count+ 1;
            msg.data= this->count;
            publisher_ -> publish(msg);

           }

rclcpp::Publisher<example_interfaces::msg::Int64>::SharedPtr publisher_;
rclcpp::TimerBase::SharedPtr timer_;


};




int main(int argc, char **argv)
{

    rclcpp::init(argc,argv);
    auto node = std::make_shared<numberpublisher>();
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;



}