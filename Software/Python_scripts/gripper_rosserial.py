#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int16


class GripperController:
    def __init__(self):
        rospy.init_node('gripper_control', anonymous=True)
        self.pub_gripper_state = rospy.Publisher('gripper_state', Int16, queue_size=3)
        # self.rate = rospy.Rate(10)  # 10hz
        self.gripper_state = Int16()
        self.gripper_state.data = 180
        self.pub_gripper_state.publish(self.gripper_state)
        print("Start control")

    def loop(self):
        while not rospy.is_shutdown():
            angle = int(input("Servo position: "))
            if 7 <= angle <= 180:
                self.gripper_state.data = angle
                self.pub_gripper_state.publish(self.gripper_state)
            else:
                print("Angle is out of range (7-180)")


def main():
    try:
        gripper = GripperController()
        gripper.loop()

    except rospy.ROSInterruptException:
        return
    except KeyboardInterrupt:
        return


if __name__ == '__main__':
    main()
