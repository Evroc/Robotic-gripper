#define USE_USBCON

#include <Wire.h>
#include <ros.h>
#include <std_msgs/Int16.h>
#include <Servo.h>

Servo servo;
ros::NodeHandle nh;


void gripperCb(const std_msgs::Int16& state)
{
  servo.write(state.data);  
}

ros::Subscriber<std_msgs::Int16> gripper_setSub("gripper_state", &gripperCb);


void setup() 
{
  nh.initNode();
  nh.subscribe(gripper_setSub);
  Serial.begin(57600);
  
  servo.attach(8);  
  servo.write(180);
}

void loop() 
{
  nh.spinOnce();
}
