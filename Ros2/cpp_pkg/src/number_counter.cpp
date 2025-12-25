#include "rclcpp/rclcpp.hpp"
#include "example_interfaces/msg/int64.hpp"

using namespace std::chrono_literals;


class number_counter : public rclcpp::Node
{
    int receivedData = 0;
    public:
        number_counter() : Node("number_counter")
        {

            subscriber_ = this->create_subscription<example_interfaces::msg::Int64>("number", 10 , 
                std::bind(&number_counter::callback_data, this , std::placeholders::_1) );

            RCLCPP_INFO(this->get_logger(),"Start Receiving Data...");

            publisher_ = this->create_publisher<example_interfaces::msg::Int64>("number_count", 10);
            timer_ = this->create_wall_timer(1s,std::bind(&number_counter::publish_data,this));

            RCLCPP_INFO(this->get_logger(),"Started publishing data");


        }


    private:
        void callback_data(const example_interfaces::msg::Int64::SharedPtr msg)
        {
            RCLCPP_INFO(this->get_logger(),"Received Data: %ld ", msg -> data);
            this->receivedData = msg->data;

        }

        void publish_data()
        {
            auto msg = example_interfaces::msg::Int64();
            msg.data = this-> receivedData;
            publisher_-> publish(msg);

        }

rclcpp::Subscription<example_interfaces::msg::Int64>::SharedPtr subscriber_;
rclcpp::Publisher<example_interfaces::msg::Int64>::SharedPtr publisher_;
rclcpp::TimerBase::SharedPtr timer_;

};



int  main(int argc, char **argv)
{
    rclcpp::init(argc,argv);
    auto node  = std::make_shared<number_counter>();
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}