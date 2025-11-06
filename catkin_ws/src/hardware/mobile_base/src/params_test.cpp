#include <ros/ros.h>

int main(int argc, char **argv) {
    ros::init(argc, argv, "my_node");
    ros::NodeHandle nh("~"); // Private NodeHandle for relative parameters
    double my_double_param;
    if (nh.getParam("my_double_param", my_double_param)) {
        ROS_INFO("Got parameter my_double_param: %f", my_double_param);
    } else {
        ROS_WARN("Parameter my_double_param not found or wrong type.");
    }
    nh.setParam("my_string_param", "some_value");
    ros::spin();
    return 0;
}
