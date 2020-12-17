#include <stdio.h>
#include <opencv2/opencv.hpp>

using namespace cv;

int main(int argc, char** argv){
	if(argc != 2){
		printf("Uso: displayImage.out <pathALaImagen>\n");
		return -1;
	}
	Mat image;
	image = imread(argv[1], 1);
	if(!image.data){
		printf("No tiene datos\n");
		return -1;
	}
	namedWindow("DisplayImage", WINDOW_AUTOSIZE);
	imshow("DisplayImage", image);
	waitKey(0);
	return 0;
}

