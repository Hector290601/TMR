#include <cv_bridge/cv_bridge.h>
#include <image_transport/image_transport.h>
#include <opencv2/highgui/highgui.hpp>
#include <ros/ros.h>
#include <sensor_msgs/image_encodings.h>

int main(int argc, char** argv)
{
    ros::init(argc, argv, "toxic_eye");
    ros::NodeHandle nh;
    int continue_flag = 1;
    std::string videoSource = "";//home/hector/car_cam_rich24_5_2023_17_23_27.avi";
    if(!nh.getParam("/toxic/camera/video_source", videoSource)){
        videoSource = "0";
    }
    nh.setParam("/toxic/camera/video_source", videoSource);
    cv::VideoCapture capture(videoSource);
    if (!capture.isOpened()) {
      ROS_ERROR_STREAM("Failed to open camera with index " << videoSource << "!");
      ros::shutdown();
    }
    image_transport::ImageTransport it(nh);
    image_transport::Publisher pub_frame = it.advertise("/toxic/camera", 1);
    cv::Mat frame;
    sensor_msgs::ImagePtr msg;
    ros::Rate loop_rate(30);
    nh.setParam("/toxic/camera/continue_video", 1);
    while (nh.ok()) {
        nh.getParam("continue_video", continue_flag);
        if(continue_flag){
            capture >> frame;
        }
        if (frame.empty()) {
            ROS_ERROR_STREAM("Failed to capture image!");
            ros::shutdown();
        }
        msg = cv_bridge::CvImage(std_msgs::Header(), "bgr8", frame).toImageMsg();
        pub_frame.publish(msg);
        //cv::imshow("camera", image);
        cv::waitKey(1);
        ros::spinOnce();
        loop_rate.sleep();
    }
    capture.release();
}
