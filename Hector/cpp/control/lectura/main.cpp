#include <iostream>
#include <wiringPi.h>

using namespace std;

int main(){
	wiringPiSetup();
	pinMode(0, OUTPUT);
	pinMode(1, INPUT);
	while(1){
		cout<<"valor: "<<digitalRead(1)<<endl;
		if(digitalRead(1)==1){
			digitalWrite(0, !digitalRead(0));
			delay(100);
		}
	}
	return 0;
}
