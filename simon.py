#!/usr/bin/python
# The humble beginnings of my Pymon Says game...
import math
import time

import Adafruit_CharLCD as LCD


# Initialize the LCD using the pins 
lcd = LCD.Adafruit_CharLCDPlate()

# Show a welcome message
lcd.message('Sup? I'm Pymon.')
time.sleep(3.0)
lcd.clear()
lcd.message('Let's start playing. Do your best! ;)')

# Show button state.
lcd.clear()
lcd.message('Press buttons...')

# Make list of button value, text, and LED color.
buttons = ( (LCD.SELECT, 'Select', (1,1,1)),
            (LCD.LEFT,   'Left/Red'  , (1,0,0)),
            (LCD.UP,     'Up/Blue'    , (0,0,1)),
            (LCD.DOWN,   'Down/Green'  , (0,1,0)),
            (LCD.RIGHT,  'Right/Yellow' , (1,1,0)) )

print 'Press Ctrl-C to quit.'
while True:
	# Loop through each button and check if it is pressed.
	for button in buttons:
		if lcd.is_pressed(button[0]):
			# Button is pressed, change the message and backlight.
			lcd.clear()
			lcd.message(button[1])
			lcd.set_color(button[2][0], button[2][1], button[2][2])
