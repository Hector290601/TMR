#include <cv_bridge/cv_bridge.h>
#include <image_transport/image_transport.h>
#include <opencv2/highgui/highgui.hpp>
#include <ros/ros.h>
#include <sensor_msgs/image_encodings.h>

int main(int argc, char** argv){
	ros::init(argc, argv, "videoPubCpp");
	ros::NodeHandle nh;
	int camera_index = 0;
	cv::VideoCapture capture(camera_index);
	if(!capture.isOpened()){
		std::cout<<"Failed to open camera"<<std::endl;
		ROS_ERROR_STREAM("Failed to open camera" << camera_index << "!");
		ros::shutdown();
	}
	std::cout<<"Success to open camera"<<std::endl;
	image_transport::ImageTransport it(nh);
	image_transport::Publisher pubFrame = it.advertise("camera", 1);
	cv::Mat frame;
	sensor_msgs::ImagePtr msg;
	ros::Rate loopRate(10);
	while(nh.ok()){
		try{
			capture >> frame;
		std::cout<<"loop"<<std::endl;
		}catch(cv::Exception ex){
			std::cout<<ex.what()<<std::endl;
			ROS_ERROR_STREAM(ex.what());
		}catch(...){
			std::cout<<"Unknow error"<<std::endl;
			ROS_ERROR_STREAM("Unknow error");
		}
		/*
		if(frame.empty()){
			ROS_ERROR_STREAM("Failed to capture image from camera " << camera_index << "!");
			ros::shutdown();
		}
		msg = cv_bridge::CvImage(std_msgs::Header(), "bgr8", frame).toImageMsg();
		pubFrame.publish(msg);
		cv::waitKey(1);
		*/
		std::cout<<"loop"<<std::endl;
		ros::spinOnce();
		loopRate.sleep();
	}
	capture.release();
}
