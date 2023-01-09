
#!/usr/bin/python3

import pygame.mixer
from gpiozero import Button
import signal
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.output(18,GPIO.LOW) #set bell stataus led to off
GPIO.setup(16,GPIO.OUT)
GPIO.output(16,GPIO.HIGH) #set power led to on after program starts

def toggle():
    GPIO.output(18,GPIO.HIGH) #light up status led during ring
    time.sleep(1)
    GPIO.output(18,GPIO.LOW) #turn off led after ring

pygame.mixer.init()

button_sounds = {Button(4): pygame.mixer.Sound("/home/pi/Desktop/door_bell_tones/doorbell-1.wav"),
Button(17): pygame.mixer.Sound("/home/pi/Desktop/door_bell_tones/doorbell-2.wav"),
Button(27): pygame.mixer.Sound("/home/pi/Desktop/door_bell_tones/doorbell-3.wav"),}

for button, sound in button_sounds.items():
    button.when_pressed = sound.play #play sound
    button.when_released = toggle #trigger led

signal.pause() #keep program alive