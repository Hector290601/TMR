#include <Servo.h>

Servo directionCar;
int directionDegree;

void setup () {
  directionCar.attach(2);
  Serial.begin(9600);
  directionCar.write(90);
}
 
void loop(){
 if (Serial.available() > 0) {
  directionDegree = Serial.parseInt();
//  if(directionDegree >= 60 and directionDegree <= 120){
    directionCar.write(directionDegree);
//  }
 }
}
