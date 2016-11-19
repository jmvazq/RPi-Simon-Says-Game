#!/usr/bin/python
# The humble beginnings of my Simon Says game...
import math
import time

import Adafruit_CharLCD as LCD

import requests


# Initialize the LCD using the pins 
lcd = LCD.Adafruit_CharLCDPlate()

# Default colors
WHITE = (1, 1, 1)
RED =  (1, 0, 0)
GREEN = (0, 1, 0)
BLUE = (0, 0, 1)
YELLOW = (1, 1, 0)

# Show startup message
def start():
	# Reset light
	lcd.set_color(WHITE[0], WHITE[1], WHITE[2])

	# Show a welcome message
	lcd.message('Sup?! I\'m Pymon.')
	time.sleep(3.0)
	lcd.clear()
	lcd.message('Let\'s start \nplaying.')

	play()

# Start game
def play():
	print 'Press Ctrl-C to quit.'
	
	# Show button state.
	time.sleep(3.0)
	lcd.clear()
	lcd.message('Press SELECT \nto start.')

	# Encouragement!
	while True:
		if lcd.is_pressed(LCD.SELECT):
			time.sleep(1.0)
			lcd.clear()
			lcd.message('Do your best! ;)')

			# Make list of button value, text, and LED color.
			buttons = ( (LCD.SELECT, 'Select', (1,1,1)),
        	    		(LCD.LEFT,   'Left/Red'  , (1,0,0)),
        	    		(LCD.UP,     'Up/Blue'    , (0,0,1)),
        	    		(LCD.DOWN,   'Down/Green'  , (0,1,0)),
        	    		(LCD.RIGHT,  'Right/Yellow' , (1,1,0)) )

			while True:
				# Loop through each button and check if it is pressed.
				for button in buttons:
					if lcd.is_pressed(button[0]):
						# Button is pressed, change the message and backlight.
						lcd.clear()
						lcd.message(button[1])
						lcd.set_color(button[2][0], button[2][1], button[2][2])

# Run code
start()
