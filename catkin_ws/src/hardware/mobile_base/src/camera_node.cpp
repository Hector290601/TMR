#include "ros/ros.h"
#include "sensor_msgs/Image.h"
#include "opencv2/opencv.hpp"
#include <cv_bridge/cv_bridge.h>

int main(int argc, char** argv)
{
  std::cout << "Initializing camera node..." << std::endl;
  ros::init(argc, argv, "camera_node");
  ros::NodeHandle n;
  ros::Rate loop(30);
  ros::Publisher pub = n.advertise<sensor_msgs::Image>("/raw_image", 10);
  
  cv::VideoCapture cap(0);
  cap.set(cv::CAP_PROP_FRAME_WIDTH , 640);
  cap.set(cv::CAP_PROP_FRAME_HEIGHT, 480);
  if(!cap.isOpened())
  {
    std::cout<< "Cannot open camera." << std::endl;
    return -1;
  }
  cv::Mat frame;
  cv_bridge::CvImage br;
  
  while(ros::ok())
  {
    cap >> br.image;
    //br.image = frame;
    pub.publish(br.toImageMsg());
    loop.sleep();
  }
  cap.release();
  return 0;
}
