#!/usr/bin/python
import menu
import BBIO
from time import sleep
import serial

print "Initialisation des peripheriques..."

BBIO.initPWM()
BBIO.initGPIO()
BBIO.initUART()

UART1 = serial.Serial(port="/dev/ttyO1", baudrate=115200, timeout=0)

mode = 'm'

print "Peripheriques initialises"

sleep(1)

while True:

	if mode == 'm':
		menu.modeManuel(UART1)
		mode = 'a'
	else:
		menu.modeAuto(UART1)
		mode = 'm'
