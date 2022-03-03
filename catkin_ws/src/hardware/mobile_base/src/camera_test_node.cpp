#include <opencv2/opencv.hpp>
#include "ros/ros.h"
#include "sensor_msgs/Image.h"
#include "std_msgs/UInt8MultiArray.h"

int main(int argc, char** argv)
{
    std::cout << "Initalizing camera-test node..." << std::endl;
    ros::init(argc, argv, "camera_test");
    ros::NodeHandle n;
    ros::Publisher pubImage = n.advertise<sensor_msgs::Image>("/rotombot/hardware/image", 1);
    ros::Publisher pubJpeg  = n.advertise<std_msgs::UInt8MultiArray>("/rotombot/hardware/img_compressed", 1);
    ros::Rate loop(60);

    // raspicam::RaspiCam_Cv cap;
    cv::VideoCapture cap(0);
    //set camera params
    /*
    cap.set( CV_CAP_PROP_FORMAT, CV_8UC3 );
    cap.set( CV_CAP_PROP_FRAME_WIDTH,320);
    cap.set( CV_CAP_PROP_FRAME_HEIGHT,240);
    cap.set( CV_CAP_PROP_ROLL,180);
    */

    if(!cap.isOpened())
    {
        std::cout << "Cannot open camera ... :'(" << std::endl;
        return -1;
    }
    
    sensor_msgs::Image msgImage;
    std_msgs::UInt8MultiArray msgCompressed;
    
    //cv::waitKey(100);
    //cv::Mat firstFrame;
    //cap >> firstFrame;
    //std::cout<<"Rows: "<<firstFrame.rows<<"  Cols: "<<firstFrame.cols <<"  ElemSize: "<<firstFrame.elemSize()<< std::endl;
    //int imageSize = firstFrame.rows*firstFrame.cols*firstFrame.elemSize();

    int img_width  = 640;
    int img_height = 480;
    msgImage.header.frame_id = "camera_link";
    msgImage.data.resize(img_width*img_height*3);
    msgImage.height = img_height;
    msgImage.width  = img_width;
    msgImage.encoding = "bgr8";
    msgImage.step = img_width*3;
    std::vector<int> compressionParams(2);
    std::vector<uchar> compressedBuff;
    compressionParams[0] = cv::IMWRITE_JPEG_QUALITY;
    compressionParams[1] = 95;


    while(ros::ok())
    {
        cap.grab();
        cv::Mat frame; 
        //cap >> frame;
	cap.retrieve(frame);
        msgImage.header.stamp = ros::Time::now();
        memcpy(msgImage.data.data(), frame.data, img_width*img_height*3);

        cv::resize(frame, frame, cv::Size(320,240));
        cv::imencode(".jpg", frame, msgCompressed.data, compressionParams);
        
        pubImage.publish(msgImage);
        pubJpeg.publish(msgCompressed);
        ros::spinOnce();
    }
    std:: cout<<"Stop camera..."<<std::endl;
    cap.release();
    return 0;
}
