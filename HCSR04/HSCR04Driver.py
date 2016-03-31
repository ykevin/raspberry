#!/usr/bin/env python
# coding: latin-1

# Autor:	kevin
# Date:		20160331
# Version:	1.0

# This module is designed to control Hcsr04 sensor get distance

import RPi.GPIO as io
import time

class HCSR04(object):

    def __init__(self, Trig, Echo):
        io.setmode(io.BCM)
        # Here we configure the GPIO settings for sensor. 
        self.trig_pin = Trig
        self.echo_pin = Echo
        self.SetupGPIO()
        # Disable warning from GPIO
        io.setwarnings(False)

    def SetupGPIO(self):
        io.setup(self.trig_pin, io.OUT, initial = False)
        io.setup(self.echo_pin, io.IN)

    def GetDistance(self):
        io.output(self.trig_pin, True)
        time.sleep(0.00015)
        io.output(self.trig_pin, False)
        while not io.input(self.echo_pin):
            pass
        t1 = time.time()
        while io.input(self.echo_pin):
            pass
        t2 = time.time()

        return (t2-t1) *340/2

# Program will clean up all GPIO settings and terminates
    def exit(self):
	io.cleanup()

