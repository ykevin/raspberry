#!/usr/bin/env python
# coding: latin-1

# Autor:	kevin
# Date:		20160331
# Version:	1.0

# This code is contorl remote car 

import lirc
import time
from L298NHBridge import HBridge


class SmartCar(object):
    def __init__(self, motors):
        self.motors = motors
        self.speed = 0
        self.arrow = "forward"
        self.status = False

    def SmartCarAction(self, codeIR):
        if codeIR == "KEY_UP":
            self.SmartCarAddSpeed()
        elif codeIR == "KEY_DOWN":
            self.SmartCarSubSpeed()
        elif codeIR == "KEY_STOP":
            self.SmartCarStop()
        elif codeIR == "KEY_START":
            self.SmartCarStart()
        elif codeIR == "KEY_GOTO":
            self.SmartCarStart()
        elif codeIR == "KEY_BACK":
            self.SmartCarBack()
        elif codeIR == "KEY_LEFT":
            self.SmartCarToLeft()
        elif codeIR == "KEY_RIGHT":
            self.SmartCarToRight()
         
    def SmartCarStart(self):
        print 'The car start move'
        self.arrow = "forward"
        if self.speed < 0:
            self.speed = 0

        if self.speed > 1:
            self.speed = 1

        for i in range(10):
            self.speed += 0.1
            if self.speed > 0.4:
                self.motors.setMotorLeft(self.speed)
                self.motors.setMotorRight(self.speed)
                time.sleep(0.5)

        self.status = True

    def SmartCarBack(self):
        print 'The car back move'
        if self.speed > 0:
            self.speed = 0
        if self.speed < -1:
            self.speed = -1
        for i in range(10):
            self.speed -= 0.1
            if self.speed < -0.4:
                self.motors.setMotorLeft(self.speed)
                self.motors.setMotorRight(self.speed)
                time.sleep(0.5)
        self.arrow = "back"
        self.status = True

    def SmartCarStop(self):
        print 'The car stop move'
        self.speed = 0
        self.status = False
        self.motors.setMotorLeft(self.speed)
        self.motors.setMotorRight(self.speed)

    def SmartCarAddSpeed(self):
        if self.status == True :
            if self.arrow == "forward":
                self.speed += 0.1
                if self.speed > 0 and self.speed < 0.4:
                    self.speed = 0.5
                if self.speed > 1:
                    self.speed = 1
            elif self.arrow == "back":
                self.speed += 0.1
                if self.speed < 0 and self.speed > -0.4:
                    self.speed = 0
                    self.arrow = "forward"

            print ('The car speed add 0.1, speed is : %0.1f' % self.speed, self.arrow)
            self.motors.setMotorLeft(self.speed)
            self.motors.setMotorRight(self.speed)
        else :
            print 'Please Start Smart Car!'

    
    def SmartCarSubSpeed(self):
        if self.status == True:
            if self.arrow == "forward":
                self.speed -= 0.1
                if self.speed > 0 and self.speed < 0.4:
                    self.speed = 0
                    self.arrow = "back"
            elif self.arrow == "back":
                self.speed -= 0.1
                if self.speed < 0 and self.speed > -0.4:
                    self.speed = -0.5
                if self.speed < -1:
                    self.speed = -1
            print ('The car speed sub 0.1, speed is : %0.1f ' % self.speed, self.arrow)
            self.motors.setMotorLeft(self.speed)
            self.motors.setMotorRight(self.speed)
        else:
            print 'Please Start Smart Car!'

    def SmartCarToRight(self):
        print 'The car right'
        if self.status == True:
            self.motors.setMotorLeft(self.speed + 0.5)
            self.motors.setMotorRight(self.speed - 0.5)

    def SmartCarToLeft(self):
        print 'The car left'
        if self.status == True:
            self.motors.setMotorLeft(self.speed - 0.5)
            self.motors.setMotorRight(self.speed + 0.5)
            
            
            
def LircDecode():
    #Init motor pin
    print "++++++Start run programe++++"
    Motors = HBridge(27, 22, 23, 24, 19, 26)
    Car = SmartCar(Motors)
    try :
        while True:
            codeIR = lirc.nextcode()
            if codeIR != []:
                Car.SmartCarAction(codeIR[0])
    except KeyboardInterrupt:
        Motors.exit()

if __name__ == "__main__":
    sockid=lirc.init("carremote", blocking = False)
    LircDecode()
