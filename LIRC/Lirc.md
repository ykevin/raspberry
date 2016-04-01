1,learn irc button
sudo /etc/init.d/lirc stop
irrecord -n -d /dev/lirc0 ~/lircd.conf

2,cp file to etc/lirc 
sudo mv ~/lircd.conf /etc/lirc/lircd.conf

3,modfiy lircd.conf file "name  /home/pi/lircd.conf" for "name programe"

4, irsend LIST programe ""

5, sudo nano ~/.lircrc 
   eg:
   begin
   		button = KEY_UP
		prog = programe
		config = KEY_UP
   end

6, sudo apt-install lirc
   write your demo code
