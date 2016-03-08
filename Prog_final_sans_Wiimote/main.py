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

while mode != 'p':

	if mode == 'm':
		mode = menu.modeManuel(UART1)
	elif mode == 'a' or mode == 'w':
		mode = menu.modeAuto(UART1)


