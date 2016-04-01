# raspberry
Some raspberry pi3 common driver python module :

1.L298N bridge driver two motors use pwm

2.Hscr04 sensor  driver get distance

3.LIRC dirver for remote control
  Init install
	1,sudo vi /boot/config.txt
	   add: doverlay=lirc-rpi
    2, sudo apt-get install lirc
	3, sudo reboot 
	4, sudo mode2 –d /dev/lirc0
	   press button for control and test module is not working
