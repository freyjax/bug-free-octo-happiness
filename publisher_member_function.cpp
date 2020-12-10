#include <chrono>
#include <memory>
#include <vector>
#include <iostream>
#include <stdlib.h>
#include "rclcpp/rclcpp.hpp"
#include "tutorial_interfaces/msg/num.hpp"     // where we store the type of msg (float64[]) 

using namespace std::chrono_literals;

int max = 10;

class MinimalPublisher : public rclcpp::Node
{
private:
	long sizeB;
	int max_count;
	int current_count;
	int msg_count = 0;
public:
  MinimalPublisher()
  : Node("minimal_publisher"), count_(0)
  {
    current_count = 0;
    sizeB = 800000;
    max_count = max;
	  hype.resize(sizeB/sizeof(hype[0])); // set size of vector
    publisher_ = this->create_publisher<tutorial_interfaces::msg::Num>("topic", 10);    // queue of 10
    timer_ = this->create_wall_timer(
      10000ms, std::bind(&MinimalPublisher::timer_callback, this)); //changed to send every 1 second to make difference more obvious
  }

private:
  void timer_callback()
  {
    auto message = tutorial_interfaces::msg::Num();                               // CHANGE
    message.num = hype;      // CHANGE
    //x = (int)malloc(999999999999999999):;
    //message.num = x;
    //
    message.num[0] = msg_count;
    RCLCPP_INFO(this->get_logger(), "message sent [%d] [%d] floats [%d] Bytes", message.num[0], message.num.size(), sizeB);    // CHANGE
    publisher_->publish(message);
    current_count++;
    msg_count++;
    if(current_count >= max_count){
    	current_count = 0;
	sizeB *= 2;
	hype.resize(sizeB/4);
	std::cout << "new size: " << sizeB << "\n";
    }
  }
  rclcpp::TimerBase::SharedPtr timer_;
  rclcpp::Publisher<tutorial_interfaces::msg::Num>::SharedPtr publisher_;         // CHANGE
  size_t count_;
  std::vector<int> hype;
};

int main(int argc, char * argv[])
{
  if (argc > 1)
	  max = atoi(argv[1]);
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<MinimalPublisher>());
  rclcpp::shutdown();
  return 0;
}
