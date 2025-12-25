#include "rclcpp/rclcpp.hpp"
#include "example_interfaces/msg/string.hpp"


class PIDcontrol : public rclcpp::Node
{
public:
    
   PIDcontrol() : Node("controlNODE")
   {

       subscriber_ = this->create_subscription<example_interfaces::msg::String>("dis_data"
        ,10,std::bind(&PIDcontrol::callback_data, this , std::placeholders::_1));

        RCLCPP_INFO(this->get_logger(),"I start receiving the data");
   }


private:

    void callback_data(const example_interfaces::msg::String::SharedPtr msg)
    {
        RCLCPP_INFO(this->get_logger(),"%s",msg->data.c_str());

    }

 rclcpp::Subscription<example_interfaces::msg::String>::SharedPtr subscriber_;

};

int main(int argc,char **argv)
{
    rclcpp::init(argc,argv); 
    auto node = std::make_shared<PIDcontrol>();
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;

}