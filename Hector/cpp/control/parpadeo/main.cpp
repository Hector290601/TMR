#include <iostream>
#include <wiringPi.h>

using namespace std;

int main(){
	wiringPiSetup();
	pinMode(0, OUTPUT);
	pinMode(1, INPUT);
	while(1){
		cout<<"valor: "<<digitalRead(0)<<endl;
		digitalWrite(0, 0);
		delay(500);
		cout<<"valor: "<<digitalRead(0)<<endl;
		digitalWrite(0, 1);
		delay(500);
	}
	return 0;
}
