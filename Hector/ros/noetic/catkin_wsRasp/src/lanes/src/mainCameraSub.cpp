#include <cv_bridge/cv_bridge.h>
#include <image_transport/image_transport.h>
#include <opencv2/highgui/highgui.hpp>
#include <ros/ros.h>
#include <sensor_msgs/image_encodings.h>

void imageCallback(const sensor_msgs::ImageConstPtr&msg){
	cv_bridge::CvImagePtr cvPtr;
	try{
		cvPtr = cv_bridge::toCvCopy(msg, "bgr8");
		cv::Mat currentFrame = cvPtr -> image;
		cv::imshow("View", currentFrame);
		cv::waitKey(30);
	}catch(cv_bridge::Exception& e){
		ROS_ERROR("Couldn't convert from %s to bgr8.", msg->encoding.c_str());

	}
}

int main(int argc, char** argv){
	ros::init(argc, argv, "videoSubCpp");
	ros::NodeHandle nh;
	image_transport::ImageTransport it(nh);
	image_transport::Subscriber sub = it.subscribe("camera", 1, imageCallback);
	ros::spin();
	cv::destroyWindow("View");
}
