import serial
import sys
import argparse


def main():
    parser = argparse.ArgumentParser(description='A test program.')
    parser.add_argument("-p", "--usb_port", help="USB port.", default="'/dev/ttyACM0'")
    args = parser.parse_args()

    try:
        arduino = serial.Serial(args.usb_port, 1600)
        print("Serial device connected!")
    except serial.SerialException as e:
        print("Wrong port!")
        print("UBB Port: ", args.usb_port)
        return 0

    while True:
        angle = int(input("Servo position: "))
        if 7 <= angle <= 180:
            arduino.write((str(angle)).encode('utf-8'))
        else:
            print("Angle is out of range (7-180)")


if __name__ == '__main__':
    main()

