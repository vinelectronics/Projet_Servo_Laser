#!/usr/bin/python
import BBIO
from time import sleep
import serial
import menu
import wiimote

BBIO.initPWM()
BBIO.initGPIO()
BBIO.initUART()

UART1 = serial.Serial(port="/dev/ttyO1", baudrate=115200, timeout=0)

sleep(1)

Rx = "\0"

UART1.flushInput()

while Rx.find('$') == -1:

	UART1.write("$\r\n")
	sleep(0.1)
	Rx = UART1.readline()

Rx = "MODE,MANU"

while Rx.find('EXIT') == -1:

	if Rx.find('MODE') != -1:

		if Rx.find('MANU') != -1:
			BBIO.mode('m')
			Rx = menu.MANUEL(UART1)
		elif Rx.find('WII,ON') != -1:
			BBIO.mode('w')
			Rx = wiimote.Wii(UART1)
		elif Rx.find('CARRE') != -1:
			BBIO.mode('a')
			Rx = menu.CARRE(UART1)
		elif Rx.find('LOSANGE') != -1:
			BBIO.mode('a')
			Rx = menu.LOSANGE(UART1)
		elif Rx.find('CERCLE') != -1:
			BBIO.mode('a')
			Rx = menu.CERCLE(UART1)

Laser = 0
H = 0
V = 0

BBIO.mode('o')
BBIO.laser(Laser)
BBIO.servomoteur1(H)
BBIO.servomoteur2(V)

UART1.close()
