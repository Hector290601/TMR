#include <ros.h> //import ros to use ros nodes
#include <std_msgs/Float64.h> // import datatype to use
#include <Servo.h> //import pwm generator lib.
ros::NodeHandle  nh; //declare node handler
Servo servo; //declare servo
unsigned long start = 0.0;

void blink_callback( const std_msgs::Float64& msg){
  float blinking = msg.data;
  if(blinking > 0.0){
    digitalWrite(6, 0);
    if(millis() >  (start + 250.0)){
      digitalWrite(4, 1);
      start = millis();
    }else{
      digitalWrite(4, 0);
    }
  }else{
    digitalWrite(4, 0);
    digitalWrite(6, 0);
  }
}

void messageCb( const std_msgs::Float64& msg){ //msg callback
  float radian = msg.data; //load msg value to a float type variable
  radian = radian + 1.5;
  if(radian > 2.1){
    radian = 2.1;
  }else if(radian < 0.9){
    radian = 0.9;
  }
  float deg = radian * (180/PI); //transform radians to degrees
  servo.write(deg);
}

ros::Subscriber<std_msgs::Float64> sub("/steering", messageCb ); //configure servo callback
ros::Subscriber<std_msgs::Float64> sub_blinking("/blinking", blink_callback ); //configure servo callback

void setup(){
  servo.attach(2); //pwm channel output to the pin 2
  servo.write(90); //initial pwm value
  pinMode(4, OUTPUT);
  pinMode(6, OUTPUT);
  nh.initNode(); //ros init node
  nh.subscribe(sub); //ros subscriber
  nh.subscribe(sub_blinking); //ros subscriber
  start = millis();
}

void loop(){
  nh.spinOnce(); //ros spin
  delay(10); //needed to set ros rate
}
