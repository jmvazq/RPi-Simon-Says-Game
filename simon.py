#!/usr/bin/python
# The humble beginnings of my Simon Says game...
import math
import time
import random

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

def reset():
	round = 0
	score = 0
	# Pattern starts as an empty list, and a random color is added to it in each round
	pattern = []
	playing = True

# Start game
def play():
	print 'Press Ctrl-C to quit.'
	
	# Request input
	time.sleep(2.0)
	lcd.clear()
	lcd.message('Press SELECT \nto start.')

	# Make tuple of button value, text, and LED color.
        BUTTONS = ( (LCD.SELECT, 'Select', (1,1,1)),
                (LCD.LEFT,   'Red!'  , (RED[0], RED[1], RED[2])),
                (LCD.UP,     'Blue!'    , (BLUE[0], BLUE[1], BLUE[2])),
                (LCD.DOWN,   'Green!'  , (GREEN[0], GREEN[1], GREEN[2])),
                (LCD.RIGHT,  'Yellow!' , (YELLOW[0], YELLOW[1], YELLOW[2]) )
        )

        # Tuple of color options for the randomly generated pattern; each color is mapped to a button
        COLORS = (BUTTONS[1], BUTTONS[2], BUTTONS[3], BUTTONS[4])

	# If SELECT is pressed
	while True:
                # The playing flag must be initialized from the very beginning
                playing = False;
		if lcd.is_pressed(LCD.SELECT) and not playing:
			# Encouragement!
			time.sleep(1.0)
			lcd.clear()
			lcd.message('Do your best! ;)')
			time.sleep(2.0)

			# Reset game values and start game
                        playing = True
                        round = 0
                        score = 0
                        pattern = []

			while playing:
				# Add random color item to pattern list, from the 4 available color options
				pattern.append(random.choice(COLORS))
				round = round + 1

				print pattern

				lcd.clear()
				lcd.message("Round " + str(round) + "\nFollow along!")
				time.sleep(2.0)

				for color in pattern:
                                        lcd.clear()
                                        lcd.message(color[1])
                                        lcd.set_color(color[2][0], color[2][1], color[2][2])
                                        time.sleep(1.5)

                                lcd.set_color(WHITE[0], WHITE[1], WHITE[2])
                                time.sleep(0.5)
                                lcd.clear()
                                lcd.message("Your turn:")

                                waiting = True
                                for color in pattern:
                                        print "Player SHOULD press " + color[1]
                                        success = False
                                        button_pressed = False
                                        while not button_pressed:
                                                for button in BUTTONS:
                                                        if lcd.is_pressed(button[0]):
                                                                print "Player pressed " + button[1]
                                                                button_pressed = True
                                                                if button[0] == color[0]:
                                                                        success = True
                                                time.sleep(0.1)
                                        if success:
                                                lcd.set_color(color[2][0], color[2][1], color[2][2])
                                                lcd.clear()
                                                lcd.message(color[1])
                                                time.sleep(1.0)
                                                continue
                                        else:
                                                time.sleep(1.0)
                                                lcd.clear()
                                                lcd.message("Oops!\nGame over. :(")
                                                time.sleep(1.0)
                                                lcd.clear()
                                                lcd.message("Your score: " + str(score) + "\nRound: " + str(round))
                                                time.sleep(2.0)

                                                lcd.clear()
                                                lcd.message("Send score? :D")
                                                time.sleep(1.0)
                                                lcd.clear()
                                                lcd.message("RED = Yes\nYELLOW = No")
                                                while True:
                                                        if lcd.is_pressed(BUTTONS[0][0]):
                                                                lcd.clear()
                                                                lcd.message("Red = YES\nYellow = NO")
                                                        if lcd.is_pressed(BUTTONS[1][0]):
                                                                lcd.clear()
                                                                lcd.message("Your name is \nANON.")
                                                                time.sleep(1.0)
                                                                lcd.clear()
                                                                lcd.message("Sending...")
                                                                lcd.clear()
                                                                start()
                                                        if lcd.is_pressed(BUTTONS[4][0]):
                                                                lcd.clear()
                                                                lcd.message("OK!\nSee you!")
                                                                time.sleep(3.0)
                                                                lcd.clear()
                                                                start()
                                                        continue
                                                continue
                                score = score + 5

# Run code
start()
