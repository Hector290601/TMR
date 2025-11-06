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
            if(!nodeHandler_.getParam("/toxic/blur/colorpsace_source", colorSpace_)){
                colorSpace_ = "/toxic/camera";
            }
            if(!nodeHandler_.getParam("/toxic/camera/blur_type", blur_type_)){
                blur_type_ = "homogeneous";
            }
            if(!nodeHandler_.getParam("/toxic/blur/kernel_size", kernel_size_)){
                kernel_size_ = 3;
            }
            if(!nodeHandler_.getParam("/toxic/blur/homogeneous/point_value", point_size_)){
                point_size_ = -1;
            }
            if(!nodeHandler_.getParam("/toxic/blur/gaussian/sigma_x", gaussian_sigma_x_)){
                gaussian_sigma_x_ = 0;
            }
            if(!nodeHandler_.getParam("/toxic/blur/gaussian/sigma_y", gaussian_sigma_y_)){
                gaussian_sigma_y_ = 0;
            }
            if(!nodeHandler_.getParam("/toxic/blur/bilateral/pixel_diameter", pixel_diameter_)){
                pixel_diameter_ = 10;
            }
            if(!nodeHandler_.getParam("/toxic/blur/bilateral/sigma_color", sigma_color_)){
                sigma_color_ = pixel_diameter_*2;
            }
            if(!nodeHandler_.getParam("/toxic/blur/bilateral/sigma_space", sigma_space_)){
                sigma_space_ = pixel_diameter_/2;
            }
            std::string publishName = "/toxic/blured" + colorSpace_;
            pub_frame = it.advertise(publishName, 1);
            nodeHandler_.setParam("/toxic/blur/colorpsace_source", colorSpace_);
            nodeHandler_.setParam("/toxic/camera/blur_type", blur_type_);
            nodeHandler_.setParam("/toxic/blur/kernel_size", kernel_size_);
            nodeHandler_.setParam("/toxic/blur/homogeneous/point_value", point_size_);
            nodeHandler_.setParam("/toxic/blur/gaussian/sigma_x", gaussian_sigma_x_);
            nodeHandler_.setParam("/toxic/blur/gaussian/sigma_y", gaussian_sigma_y_);
            nodeHandler_.setParam("/toxic/blur/bilateral/pixel_diameter", pixel_diameter_);
            nodeHandler_.setParam("/toxic/blur/bilateral/sigma_color", sigma_color_);
            nodeHandler_.setParam("/toxic/blur/bilateral/sigma_space", sigma_space_);
            sub = it.subscribe(colorSpace_, 1, &BilateralNode::imageCallback, this);
            std::cout << "Node initialized" << std::endl;
        }

        void imageCallback(const sensor_msgs::ImageConstPtr& msg){
            original_image = cv_bridge::toCvShare(msg, "bgr8")->image;
            if(blur_type_ == "homogeneous"){
                blur( original_image, blured_image, cv::Size(kernel_size_, kernel_size_), cv::Point(point_size_, point_size_) );
            }else if(blur_type_ == "gaussian"){
                GaussianBlur( original_image, blured_image, cv::Size( kernel_size_, kernel_size_), gaussian_sigma_x_, gaussian_sigma_y_ );
            }else if(blur_type_ == "median"){
                medianBlur ( original_image, blured_image, kernel_size_ );
            }else if(blur_type_ == "bilateral"){
                bilateralFilter ( original_image, blured_image, pixel_diameter_, sigma_color_, sigma_space_ );
            }
            switch(blured_image.channels()){
                case 1:
                    channels_ = "mono8";
                break;
                case 3:
                    channels_ = "bgr8";
                break;
            }
            publishImg = cv_bridge::CvImage(std_msgs::Header(), channels_, blured_image).toImageMsg();
            pub_frame.publish(publishImg);
        }

    private:
        ros::NodeHandle nodeHandler_;
        cv::Mat original_image;
        cv::Mat blured_image;
        std::string colorSpace_;
        std::string blur_type_;
        std::string channels_;
        int kernel_size_;
        int point_size_;
        int gaussian_sigma_x_;
        int gaussian_sigma_y_;
        int pixel_diameter_;
        double sigma_color_;
        double sigma_space_;
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
