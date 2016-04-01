#!/usr/bin/python 

from HSCR04Driver import HCSR04
import time


if __name__ == "__main__":
    Sensor = HCSR04(17, 18)
    try:
        while True:
            print 'Distance:%0.2f m' % Sensor.GetDistance()
            time.sleep(2)
    except KeyboardInterrupt:
        Sensor.exit()


