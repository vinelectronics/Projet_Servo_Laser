#!/usr/bin/python
import BBIO
from time import sleep
import serial
import menu

BBIO.initPWM()
BBIO.initGPIO()
BBIO.initUART()

UART1 = serial.Serial(port="/dev/ttyO1", baudrate=115200, timeout=0)

Rx = "MODE,MANU"

sleep(1)

while Rx.find('EXIT') == -1:

	if Rx.find('MODE') != -1:

		if Rx.find('MANU') != -1:
			Rx = menu.MANUEL(UART1)
		elif Rx.find('WII') != -1:
			Rx = menu.WII(UART1)
		elif Rx.find('CARRE') != -1:
			Rx = menu.CARRE(UART1)
		elif Rx.find('LOSANGE') != -1:
			Rx = menu.LOSANGE(UART1)
		elif Rx.find('CERCLE') != -1:
			Rx = menu.CERCLE(UART1)
