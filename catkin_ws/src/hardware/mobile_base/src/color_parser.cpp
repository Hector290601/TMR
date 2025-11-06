#include <ros/ros.h>
#include <sensor_msgs/Image.h>
#include <opencv2/opencv.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <image_transport/image_transport.h>
#include <cv_bridge/cv_bridge.h>
#include <iostream>
#include <opencv2/imgproc.hpp>

class BilateralNode{
    public:
        BilateralNode()
            : it(nodeHandler_)
        {
            std::cout << "Initializing color parser node..." << std::endl;
            colorSpace_ = "";
            if(!nodeHandler_.getParam("/toxic/camera/colorpsace_goal", colorSpace_)){
                colorSpace_ = "gray";
            }
            if(colorSpace_ == "gray"){
                colorSpace_cv_ = cv::COLOR_BGR2GRAY; channels_ = "mono8";
            }else if(colorSpace_ == "hsv"){
                colorSpace_cv_ = cv::COLOR_BGR2HSV;
                channels_ = "bgr8";
            }else if(colorSpace_ == "hls"){
                colorSpace_cv_ = cv::COLOR_BGR2HLS;
                channels_ = "bgr8";
            }
            std::string publishName = "/toxic/camera/colorpsace_goal/" + colorSpace_;
            pub_frame = it.advertise(publishName, 1);
            nodeHandler_.setParam("/toxic/camera/colorpsace_goal", colorSpace_);
            sub = it.subscribe("/toxic/camera", 1, &BilateralNode::imageCallback, this);
            std::cout << "Node initialized" << std::endl;
        }

        void imageCallback(const sensor_msgs::ImageConstPtr& msg){
            original_image = cv_bridge::toCvShare(msg, "bgr8")->image;
            cv::cvtColor(original_image, parsed_image, colorSpace_cv_);
            publishImg = cv_bridge::CvImage(std_msgs::Header(), channels_, parsed_image).toImageMsg();
            pub_frame.publish(publishImg);
        }

    private:
        ros::NodeHandle nodeHandler_;
        cv::Mat original_image;
        cv::Mat parsed_image;
        std::string colorSpace_;
        std::string channels_;
        int colorSpace_cv_;
        image_transport::ImageTransport it;
        image_transport::Publisher pub_frame;
        image_transport::Subscriber sub;
        sensor_msgs::ImagePtr publishImg;
};

int main(int argc, char** argv) {
    ros::init(argc, argv, "colorParser");
    BilateralNode colorParserNode;
    ros::spin();
    return 0;
}
