#include "rclcpp/rclcpp.hpp"
#include "example_interfaces/msg/string.hpp"

using namespace std::chrono_literals;

class DistanceSensor : public rclcpp::Node {
public:
    DistanceSensor() 
    : Node("distance_sensor"), robot_name_("Dhoosan M1")  // Default robot name
    {
        this->declare_parameter<std::string>("robot_name", robot_name_);
        this->get_parameter("robot_name", robot_name_);
        
        publisher_ = this->create_publisher<example_interfaces::msg::String>("dis_data", 10);
        timer_ = this->create_wall_timer(0.5s, std::bind(&DistanceSensor::publishData, this));

        RCLCPP_INFO(this->get_logger(), "Data publishing started for robot: %s", robot_name_.c_str());
    }

private:
    void publishData()
    {
        auto msg = example_interfaces::msg::String();
        msg.data = "This is " + robot_name_;
        publisher_->publish(msg);
    }

    std::string robot_name_;
    rclcpp::Publisher<example_interfaces::msg::String>::SharedPtr publisher_;
    rclcpp::TimerBase::SharedPtr timer_;
};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<DistanceSensor>();
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}
