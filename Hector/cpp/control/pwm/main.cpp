#include <iostream>
#include <wiringPi.h>

using namespace std;
unsigned int prevTime;

int main(){
	wiringPiSetup();
	pinMode(1, PWM_OUTPUT);
	for(int i = 0; i < 1024; i+=1){
		cout<<i<<endl;
		pwmWrite(1, i);
		delay(1);
	}
	for(int i = 1020; i > 0; i-=1){
		cout<<i<<endl;
		pwmWrite(1, i);
		delay(1);
	}
	return 0;
}
