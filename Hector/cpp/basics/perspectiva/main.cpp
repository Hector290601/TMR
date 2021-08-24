#include <stdio.h>
#include <iostream>
#include <opencv2/core.hpp>
#include <opencv2/videoio.hpp>
#include <opencv2/highgui.hpp>

using namespace cv;
using namespace std;

int main(int, char**){
	Mat frame;
	VideoCapture cap;
	int device = 0;
	int apiId = cv::CAP_ANY;
	cap.open(device, apiId);
	if(!cap.isOpened()){
		cerr << "ERRO! UNABLE TO OPEN CAMERA DEVICE\n";
		return -1;
	}
	cout << "Iniciando"<<endl
	<<"Press any key to end"<<endl;
	for(;;){
		cap.read(frame);
		if(frame.empty()){
			cerr <<"ERROR!, BLANK FRAME\n";
			break;
		}
		imshow("videoCapture", frame);
		if(waitKey(5) >= 0){
			break;
		}
	}
	return 0;
}

