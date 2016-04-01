#!/usr/bin/env python
# coding: latin-1

# Autor:	kevin
# Date:		20160331
# Version:	1.0

# This code is contorl remote car 

import lirc
import time
from L298NHBridge import HBridge

#Init motor pin
Motors = HBridge(27, 22, 23, 24, 19, 26)

global speed
global arrow
speed = 0
arrow = "forward"

def SmartCarStart():
    print 'The car start move '
    global speed
    global arrow 
    arrow = "forward"
    if speed < 0:
        speed = 0
    if speed > 1:
        speed = 1
    for i in range(10) :
        speed = speed + 0.1
        if speed > 0.4 :
            Motors.setMotorLeft(speed)
            Motors.setMotorRight(speed)
            time.sleep(0.5)

def SmartCarBack():
    print 'The car back'
    global speed
    global arrow 
    arrow = "back"
    if speed > 0 :
        speed = 0
    if speed < -1:
        speed = -1
    for i in range(10) :
        speed = speed - 0.1
        if speed < -0.4 :
            Motors.setMotorLeft(speed)
            Motors.setMotorRight(speed)
            time.sleep(0.5)
    
def SmartCarStop():
    print 'The car stop move'
    global speed
    speed = 0
    Motors.setMotorLeft(speed)
    Motors.setMotorRight(speed)

def SmartCarAddSpeed():
    global speed
    global arrow
    if arrow == "forward" :
        speed = speed + 0.1
        if speed > 0 and speed < 0.4:
            speed = 0.5
        if speed > 1:
            speed = 1
    elif arrow == "back":
        speed = speed - 0.1
        if speed < 0 and speed > -0.4 :
            speed = -0.5
        if speed < -1:
            speed = -1

    print ('The car speed add 0.1, speed is : %0.1f' % speed)
    Motors.setMotorLeft(speed)
    Motors.setMotorRight(speed)

def SmartCarSubSpeed():
    global speed
    global arrow

    if arrow == "forward" :
        speed = speed - 0.1
        if speed > 0 and speed < 0.4 :
            speed = 0
    elif arrow == "back":
        speed = speed + 0.2
        if speed < 0 and speed > -0.4:
            speed = 0;
    
    print ('The car speed sub 0.1, speed is : %0.1f ' % speed)
    Motors.setMotorLeft(speed)
    Motors.setMotorRight(speed)


def LircDecode():
    print "++++++Start run programe++++"
    try :
        while True:
            codeIR = lirc.nextcode()
            if codeIR != []:
                if codeIR[0] == "KEY_UP":
                    SmartCarAddSpeed()
                elif codeIR[0] == "KEY_DOWN":
                    SmartCarSubSpeed()
                elif codeIR[0] == "KEY_STOP":
                    SmartCarStop()
                elif codeIR[0] == "KEY_START":
                    SmartCarStart()
                elif codeIR[0] == "KEY_GOTO":
                    SmartCarStart()
                elif codeIR[0] == "KEY_BACK":
                    SmartCarBack()
                elif codeIR[0] == "KEY_LEFT":
                    print 'The car left'
                elif codeIR[0] == "KEY_RIGHT":
                    print 'The car right'
    except KeyboardInterrupt:
        Motors.exit()

if __name__ == "__main__":
    sockid=lirc.init("carremote", blocking = False)
    LircDecode()
