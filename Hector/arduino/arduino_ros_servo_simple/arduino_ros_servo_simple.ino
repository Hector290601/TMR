#include <ros.h> //import ros to use ros nodes
#include <std_msgs/Float64.h> // import datatype to use
#include <Servo.h> //import pwm generator lib.
ros::NodeHandle  nh; //declare node handler
Servo servo; //declare servo

void messageCb( const std_msgs::Float64& msg){ //msg callback
  float radian = msg.data; //load msg value to a float type variable
  radian = radian + 1.5;
  if(radian > 2.1){
    radian = 2.1;
  }else if(radian < 0.9){
    radian = 0.9;
  }
  float deg = radian * (180/PI); //transform radians to degrees
  if(deg > 120){ //lower limit
    servo.write(120); 
  }else if(deg < 60){ //upper limit
    servo.write(60);
  }else{ //write readed value
    servo.write(deg);
  }
}

ros::Subscriber<std_msgs::Float64> sub("/steering", messageCb ); //configure servo callback

void setup(){
  servo.attach(2); //pwm channel output to the pin 2
  servo.write(90); //initial pwm value
  nh.initNode(); //ros init node
  nh.subscribe(sub); //ros subscriber
}

void loop(){
  nh.spinOnce(); //ros spin
  delay(10); //needed to set ros rate
}
