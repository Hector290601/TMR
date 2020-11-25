#include <Servo.h>

int lPwm = 5;
int rPwm = 6;
int enableMotor = 8;
Servo directionCar;
int directionDegree;

void setup () {
  directionCar.attach(9);
  directionCar.write(90);
  pinMode(lPwm, OUTPUT);
  pinMode(rPwm, OUTPUT);
  pinMode(enableMotor, OUTPUT);
  digitalWrite(lPwm, 0);
  digitalWrite(rPwm, 0);
  digitalWrite(enableMotor, 0);
  Serial.begin(9600);
}
 
void loop(){
 if(Serial.available() > 0){
   directionDegree = Serial.parseInt();
   if(directionDegree != 255){
     directionCar.write(directionDegree);
   }else{
     directionCar.write(90);
   }
 }
 if(directionDegree == 90){
   digitalWrite(enableMotor, 1);
   analogWrite(lPwm, 20);
   analogWrite(rPwm, 0);
   Serial.print(directionDegree);
 }else if(directionDegree == 60 || directionDegree == 120){
   digitalWrite(enableMotor, 1);
   analogWrite(lPwm, 20);
   analogWrite(rPwm, 0);
   Serial.print(directionDegree);
 }else if(directionDegree == 255){
   analogWrite(lPwm, 0);
   analogWrite(rPwm, 0);
   Serial.print(directionDegree);
 }else{
   analogWrite(lPwm, 0);
   analogWrite(rPwm, 30);
   digitalWrite(enableMotor, 0);
   Serial.print(directionDegree);
 }
}
