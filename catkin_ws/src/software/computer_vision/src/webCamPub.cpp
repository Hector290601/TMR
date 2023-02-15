#include <cv_bridge/cv_bridge.h>
#include <image_transport/image_transport.h>
#include <opencv2/highgui/highgui.hpp>
#include <ros/ros.h>
#include <sensor_msgs/image_encodings.h>

int main(int argc, char** argv){
	ros::init(argc, argv, "videoPubCpp");
	ros::NodeHandle nh;
	const int cameraIndex = 0;
	cv::VideoCapture capture(0);
	if(!capture.isOpened()){
		ROS_ERROR_STREAM("Failed to open camera" << cameraIndex << "!");
		ros::shutdown();
	}
	image_transport::ImageTransport it(nh);
	image_transport::Publisher pubFrame = it.advertise("camera", 1);
	cv::Mat frame;
	sensor_msgs::ImagePtr msg;
	ros::Rate loopRate(60);
	while(nh.ok()){
		capture >> frame;
		if(frame.empty()){
			ROS_ERROR_STREAM("Failed to capture image from camera " << cameraIndex << "!");
			ros::shutdown();
		}
		msg = cv_bridge::CvImage(std_msgs::Header(), "bgr8", frame).toImageMsg();
		pubFrame.publish(msg);
		cv::waitKey(1);
		ros::spinOnce();
		loopRate.sleep();
	}
	capture.release();
}
