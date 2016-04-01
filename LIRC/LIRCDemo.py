#!/usr/bin/env python
# coding: latin-1

# Autor:	kevin
# Date:		20160331
# Version:	1.0

# This module is designed to control Hcsr04 sensor get distance

import lirc
import time
from L298NHBridge import HBridge

def LircDecode():
    print "++++++Start run programe++++"
    Motors = HBridge(27, 22, 23, 24, 19, 26)
    try :
        while True:
            codeIR = lirc.nextcode()
            if codeIR != []:
                if codeIR[0] == "KEY_UP":
                    print 'The car speed add 0.1'
                elif codeIR[0] == "KEY_DOWN":
                    print 'The car speed sub 0.1'
                elif codeIR[0] == "KEY_STOP":
                    print 'The car stop move'
                    Motors.setMotorLeft(0)
                    Motors.setMotorRight(0)
                elif codeIR[0] == "KEY_START":
                    print 'The car start move '
                    Motors.setMotorLeft(1)
                    Motors.setMotorRight(1)
                elif codeIR[0] == "KEY_GOTO":
                    print 'The car forward'
                elif codeIR[0] == "KEY_BACK":
                    print 'The car back'
                elif codeIR[0] == "KEY_LEFT":
                    print 'The car left'
                elif codeIR[0] == "KEY_RIGHT":
                    print 'The car right'
    except KeyboardInterrupt:
        Motors.exit()

if __name__ == "__main__":
    sockid=lirc.init("carremote", blocking = False)
    LircDecode()
