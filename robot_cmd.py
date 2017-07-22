import os
import sys    
import termios
import fcntl
import RPi.GPIO as gpio
import time
import random



def getch():
  import sys, tty, termios
  init()
  sleep_time = 0.050
  old_settings = termios.tcgetattr(0)
  new_settings = old_settings[:]
  new_settings[3] &= ~termios.ICANON
  try:
    termios.tcsetattr(0, termios.TCSANOW, new_settings)
    ch = sys.stdin.read(1)
    if (ch == 'w'):
        forward(sleep_time)
    elif ch == 's':
        reverse(sleep_time)
    elif ch == 'a':
        turn_left(sleep_time)
    elif ch == 'd':
        turn_right(sleep_time)
    elif ch == 'q':
        pivot_left(sleep_time)
    elif ch == 'e':
        pivot_right(sleep_time)
    elif ch == 'x':
        clean_up() 
        sys.exit()
    else:
        clean_up()
        pass
    init()
    if(gpio.input(21)==1):
      forward(sleep_time)
      
  finally:
    termios.tcsetattr(0, termios.TCSANOW, old_settings)
  return ch


def init():
    gpio.setmode(gpio.BOARD)
    gpio.setup(7, gpio.OUT)
    gpio.setup(11, gpio.OUT)
    gpio.setup(13, gpio.OUT)
    gpio.setup(15, gpio.OUT)
    gpio.setup(16, gpio.OUT)
    gpio.setup(18, gpio.OUT)
    gpio.setup(21, gpio.IN)
    gpio.output(16, True)    

def forward(tf):
    gpio.output(7, False)
    gpio.output(11, True)
    gpio.output(13, True)
    gpio.output(15, False)
    time.sleep(tf)
    clean_up()
    

def reverse(tf):
    gpio.output(7, True)
    gpio.output(11, False)
    gpio.output(13, False)
    gpio.output(15, True)
    time.sleep(tf)
    clean_up()

def turn_left(tf):
    gpio.output(7, False)
    gpio.output(11, False)
    gpio.output(13, True)
    gpio.output(15, False)
    time.sleep(tf)
    clean_up()

def turn_right(tf):
    gpio.output(7, False)
    gpio.output(11, True)
    gpio.output(13, False)
    gpio.output(15, False)
    time.sleep(tf)
    clean_up()

def pivot_left(tf):
    gpio.output(7, False)
    gpio.output(11, True)
    gpio.output(13, False)
    gpio.output(15, True)
    time.sleep(tf)
    clean_up()

def pivot_right(tf):
    gpio.output(7, True)
    gpio.output(11, False)
    gpio.output(13, True)
    gpio.output(15, False)
    time.sleep(tf)
    clean_up()

def clean_up():
    gpio.output(7, False)
    gpio.output(11, False)
    gpio.output(13, False)
    gpio.output(15, False)
    gpio.output(16, False)
    gpio.cleanup()   


def main():
  
  while True:
        print("\nKey: '" + getch() + "'\n")
      



if __name__ == "__main__":
    main()


