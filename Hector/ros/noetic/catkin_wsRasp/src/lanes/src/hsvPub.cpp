#include <cv_bridge/cv_bridge.h>
#include <image_transport/image_transport.h>
#include <opencv2/highgui/highgui.hpp>
#include <ros/ros.h>
#include <sensor_msgs/image_encodings.h>
void imageCallback(const sensor_msgs::ImageConstPtr& msg){
	cv_bridge::CvImagePtr cvPtr;
	try{
		ros::NodeHandle node;
		cvPtr = cv_bridge::toCvCopy(msg, "bgr8");
		cv::Mat currentFrame = cvPtr -> image;
		cv::Mat hsvImage;
		cv::cvtColor(currentFrame, hsvImage, cv::COLOR_BGR2HSV);
		image_transport::ImageTransport it(node);
		image_transport::Publisher pubFrame = it.advertise("hsv", 1);
		sensor_msgs::ImagePtr msg;
		msg = cv_bridge::CvImage(std_msgs::Header(), "bgr8", hsvImage).toImageMsg();
		pubFrame.publish(msg);
		cv::waitKey(30);
	}catch(cv_bridge::Exception& e){
		ROS_ERROR("Couldn't convert from %s to bgr8.", msg->encoding.c_str());

	}
}

int main(int argc, char** argv){
	ros::init(argc, argv, "hsvConverter");
	ros::NodeHandle nh;
	image_transport::ImageTransport it(nh);
	image_transport::Subscriber sub = it.subscribe("camera", 1, imageCallback);
	ros::spin();
	cv::destroyWindow("Hsv");
}
/*
int main(int argc, char** argv){
	ros::NodeHandle nh;
	ros::init(argc, argv, "hsvConverter");
	image_transport::ImageTransport it(nh);
	image_transport::Subscriber sub = it.subscribe("camera", 1);
	cv_bridge::CvImagePtr cvPtr;
	try{
		cvPtr = cv_bridge::toCvCopy(msg, "bgr8");
		cv::Mat currentFrame = cvPtr -> image;
		cv::Mat hsvImage;
		cv::cvtColor(currentFrame, hsvImage, cv::COLOR_BGR2HSV);
		image_transport::ImageTransport it(nh);
		image_transport::Publisher pub = it.advertise("hsv", 1);
		sensor_msgs::ImagePtr msg;
		msg = cv_bridge::CvImage(std_msgs::Header(), "bgr8", hsvImage).toImageMsg();
		pub.publish(msg);
		cv::waitKey(30);
	}catch(cv_bridge::Exception& e){
		ROS_ERROR("Couldn't convert image to bgr8.");
	}
	ros::spin();
	cv::destroyWindow("Hsv");
}
*/
