# Robotic gripper

## Table of contents
  1. [Introduction](#introduction)
  1. [Features](#features)
  1. [Printed parts](#printed-parts) 
  1. [Other parts](#other-parts)
  1. [PCB](#pcb)
  1. [Software](#software)
  1. [Simulation](#simulation)
  1. [Assembly manual](#assembly-manual)
  1. [Additional informations](#additional-informations)
  1. [Other links](#other-links)

## Introduction

 Cheap, 3d printed gripper for robotic applications with integrated electronics and ROS communication.
    
<img src="https://github.com/Evroc/Robotic-gripper/blob/main/Gripper/Images/gripperOnUR_1.jpg" alt="Gripper mounted on UR3e" width="700"/>

    
## Features

* The gripper is mostly 3D printed, all parts were designed for FDM printers.

* Cheap - <100$ (excluding 3d printed parts), the most expensive parts are servomechanism and microcontroller.

* Powerful grip - 2:1 gear ratio.

* Plug’n play - after assembling the project all you need to do is connect a USB-C cable and power cord
to DC socket.

* Easy communication - you can simply send the servo position using a USB-C cable and provided code
example.

* ROS compatible - use rosserial to communicate with the gripper.

## Printed parts

All files can be found there: ([LINK](https://www.printables.com/model/165722-robotic-gripper))

## Other parts
  
For non printed parts look here:

* Gripper parts [CLICK](/Gripper/BOM/GripperBOM.xlsx)

* PCB parts [CLICK](/PCB/BOM/PCB_BOM.xlsx)

## PCB

I designed dedicated PCB for this project, however feel free to modify it or even use your own designs.
<img src="https://github.com/Evroc/Robotic-gripper/blob/main/PCB/Images/PCB_photo.jpg" alt="PCB" width="350"/>
  
 Cheatsheet:
 * STATUS led - pin 0 (pinMode(0, OUTPUT))
 * COMMUNICATION led - pin 1 (pinMode(1, OUTPUT))
 * SERVO - pin 8 (servo.attach(8))
 * Power Status led works independently from the software
 * Jumper allows to power MCU without USB cable
  
<img src="https://github.com/Evroc/Robotic-gripper/blob/main/PCB/Images/PCB_connectors.PNG" alt="PCB" width="350"/> 
  


## Software

The repository includes two exemplary control methods:
- using the serial library
- using the rosserial package and the ROS platform

The included examples are written in Python language.

In order to upload the program to Seeeduino, the appropriate Arduino IDE configuration is necessary ([instruction](http://wiki.ros.org/ROS/Installation))

For both options it is necessary to install the pyserial library:
```
$ pip3 install pyserial
```
To use example with pyserial:
* upload to Seeeduino program gripper_serial.ino
* run the script gripper_serial.py with the appropriate port as an argument:
```
$ python3 gripper_serial.py --usb_port /dev/ttyACM0
```

To use example with rosserial: 
* upload to Seeeduino program gripper_rosserial.ino
* install ROS ([installation instruction](http://wiki.ros.org/ROS/Installation))
* create a workspace and build rosserial repository:
```
$ mkdir -p catkin_ws/src
$ cd /catkin_ws/src
$ git clone https://github.com/ros-drivers/rosserial.git
$ cd /catkin_ws
$ catkin_make
$ source devel/setup.bash
```
* run roscore in another terminal
* run serial_node with the appropriate port as an argument:
```
$ rosrun rosserial_python serial_node.py port:=dev/ttyACM0
```
* in another terminal run script gripper_rosserial.py
* you can also control gripper by publish state on the topic /gripper_state, for example:
```
$ rostopic pub /gripper_state std_msgs/Int16 "data: 0"
```
## Simulation

Check that: https://github.com/Michal-Bidzinski/UR3_sim

## Assembly manual
  
Online version is here: ([Build guide](https://1drv.ms/p/s!AmhhxRqSkzTrhK5689f8yG8gnyS89Q?e=EBmXII)) 
  
PDF is here: [Build guide PDF](/Build_guide/GripperBuildGuide_v1.0.pdf)

  
## Additional informations
  
Keep in mind that the project is still under development and some information is missing here. If you encounter problems - contact me using email: michael.grabowski.lab@gmail.com
  
## Other links

  ([Assembly animation](https://www.youtube.com/watch?v=25BgIXnhyFg))
  
  ([How does the mechanism works](https://youtu.be/p2rVJ_NBgKo))

