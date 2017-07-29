# Auto-run
1) At the command prompt or in a terminal window type :
sudo raspi-config
2) Select “Boot Options”
3) In the command prompt or in a terminal window type :
sudo nano /etc/profile
4) Scroll to the bottom and add the following line :
sudo python /home/pi/Desktop/robotics/robot_cmd2.py
5) Type “Ctrl+X” to exit, then “Y” to save followed by “Enter” twice.
6) To test if this has worked reboot your Pi using :
sudo reboot