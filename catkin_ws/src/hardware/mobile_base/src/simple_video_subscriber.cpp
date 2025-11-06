#include <ros/ros.h>
#include <sensor_msgs/Image.h>
#include <opencv2/opencv.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <image_transport/image_transport.h>
#include <cv_bridge/cv_bridge.h>
#include <iostream>

void imageCallback(const sensor_msgs::ImageConstPtr& msg){
    try{
        cv::imshow("view", cv_bridge::toCvShare(msg, "bgr8")->image);
        cv::waitKey(30);
    }catch (cv_bridge::Exception& e){
        ROS_ERROR("Could not convert from '%s' to 'bgr8'.", msg->encoding.c_str());
    }
}

int main(int argc, char** argv)
{
    std::cout << "Initializing camera node..." << std::endl;
    ros::init(argc, argv, "camera_view");
    ros::NodeHandle n;
    image_transport::ImageTransport it(n);
    image_transport::Subscriber sub = it.subscribe("/toxic/camera", 1, imageCallback);
    ros::spin();
    return 0;
}
