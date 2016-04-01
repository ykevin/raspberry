#!/usr/bin/env python
# coding: latin-1

# Autor:	kevin
# Date:		20160331
# Version:	1.0
#Thanks for origin Autor's Ingmar Stape 

# This module is designed to control two motors with a L298N H-Bridge

# Use this module by creating an instance of the class. To do so call the Init function, then command as desired, e.g.
# import L298NHBridge
# HBridge = L298NHBridge.L298NHBridge()
# HBridge.Init()

# Import the libraries the class needs
import RPi.GPIO as io
import time

class HBridge(object):

    def __init__(self, left_pin1, left_pin2, right_pin1, right_pin2, leftpwm_pin, rightpwm_pin):
        io.setmode(io.BCM)
        # Constant values
        self.PWM_MAX = 100
        # Here we configure the GPIO settings for the left and right motors spinning direction. 
        # It defines the four GPIO pins used as input on the L298 H-Bridge to set the motor mode (forward, reverse and stopp).
        self.leftmotor_in1_pin = left_pin1
        self.leftmotor_in2_pin = left_pin2
        self.rightmotor_in1_pin = right_pin1
        self.rightmotor_in2_pin = right_pin2
        self.leftmotorpwm_pin = leftpwm_pin
        self.rightmotorpwm_pin = rightpwm_pin
        self.SetupGPIO()
        self.leftmotorpwm = io.PWM(self.leftmotorpwm_pin,100)
        self.rightmotorpwm = io.PWM(self.rightmotorpwm_pin,100)
        self.InitPWM()
        # Disable warning from GPIO
        io.setwarnings(False)

    def SetupGPIO(self):
        io.setup(self.rightmotor_in1_pin, io.OUT)
        io.setup(self.rightmotor_in2_pin, io.OUT)
        io.setup(self.leftmotor_in1_pin, io.OUT)
        io.setup(self.leftmotor_in2_pin, io.OUT)
        io.setup(self.leftmotorpwm_pin, io.OUT)
        io.setup(self.rightmotorpwm_pin, io.OUT)

    def InitPWM(self): 
        # Here we configure the GPIO settings for the left and right motors spinning speed. 
        # It defines the two GPIO pins used as input on the L298 H-Bridge to set the motor speed with a PWM signal.
        self.leftmotorpwm.start(0)
        self.leftmotorpwm.ChangeDutyCycle(0)
        self.rightmotorpwm.start(0)
        self.rightmotorpwm.ChangeDutyCycle(0)
    
    def resetMotorGPIO(self):
        io.output(self.leftmotor_in1_pin, False)
        io.output(self.leftmotor_in2_pin, False)
        io.output(self.rightmotor_in1_pin, False)
        io.output(self.rightmotor_in2_pin, False)

# setMotorMode()

# Sets the mode for the L298 H-Bridge which motor is in which mode.

# This is a short explanation for a better understanding:
# motor		-> which motor is selected left motor or right motor
# mode		-> mode explains what action should be performed by the H-Bridge

# setMotorMode(leftmotor, reverse)	-> The left motor is called by a function and set into reverse mode
# setMotorMode(rightmotor, stopp)	-> The right motor is called by a function and set into stopp mode
    def setMotorMode(self, motor, mode):

	if motor == "leftmotor":
	    if mode == "reverse":
		io.output(self.leftmotor_in1_pin, True)
		io.output(self.leftmotor_in2_pin, False)
	    elif  mode == "forward":
		io.output(self.leftmotor_in1_pin, False)
		io.output(self.leftmotor_in2_pin, True)
	    else:
		io.output(self.leftmotor_in1_pin, False)
		io.output(self.leftmotor_in2_pin, False)
			
	elif motor == "rightmotor":
	    if mode == "reverse":
		io.output(self.rightmotor_in1_pin, False)
		io.output(self.rightmotor_in2_pin, True)		
	    elif  mode == "forward":
		io.output(self.rightmotor_in1_pin, True)
		io.output(self.rightmotor_in2_pin, False)		
	    else:
		io.output(self.rightmotor_in1_pin, False)
		io.output(self.rightmotor_in2_pin, False)
	else:
            self.resetMotorGPIO()

# SetMotorLeft(power)

# Sets the drive level for the left motor, from +1 (max) to -1 (min).

# This is a short explanation for a better understanding:
# SetMotorLeft(0)     -> left motor is stopped
# SetMotorLeft(0.75)  -> left motor moving forward at 75% power
# SetMotorLeft(-0.5)  -> left motor moving reverse at 50% power
# SetMotorLeft(1)     -> left motor moving forward at 100% power
    def setMotorLeft(self, power):
	if power < 0:
	    # Reverse mode for the left motor
	    self.setMotorMode("leftmotor", "reverse")
	    pwm = -int(self.PWM_MAX * power)
	    if pwm > self.PWM_MAX:
		pwm = self.PWM_MAX
	elif power > 0:
	    # Forward mode for the left motor
	    self.setMotorMode("leftmotor", "forward")
	    pwm = int(self.PWM_MAX * power)
	    if pwm > self.PWM_MAX:
		pwm = self.PWM_MAX
	else:
	    # Stopp mode for the left motor
	    self.setMotorMode("leftmotor", "stopp")
	    pwm = 0
#	print "SetMotorLeft", pwm
	self.leftmotorpwm.ChangeDutyCycle(pwm)

# SetMotorRight(power)

# Sets the drive level for the right motor, from +1 (max) to -1 (min).

# This is a short explanation for a better understanding:
# SetMotorRight(0)     -> right motor is stopped
# SetMotorRight(0.75)  -> right motor moving forward at 75% power
# SetMotorRight(-0.5)  -> right motor moving reverse at 50% power
# SetMotorRight(1)     -> right motor moving forward at 100% power
    def setMotorRight(self, power):
	if power < 0:
	    # Reverse mode for the right motor
	    self.setMotorMode("rightmotor", "reverse")
	    pwm = -int(self.PWM_MAX * power)
	    if pwm > self.PWM_MAX:
		pwm = self.PWM_MAX
	elif power > 0:
	    # Forward mode for the right motor
	    self.setMotorMode("rightmotor", "forward")
	    pwm = int(self.PWM_MAX * power)
	    if pwm > self.PWM_MAX:
	        pwm = self.PWM_MAX
	else:
	    # Stopp mode for the right motor
	    self.setMotorMode("rightmotor", "stopp")
	    pwm = 0
        #print "SetMotorRight", pwm
	self.rightmotorpwm.ChangeDutyCycle(pwm)

# Program will clean up all GPIO settings and terminates
    def exit(self):
        self.resetMotorGPIO()
	io.cleanup()

