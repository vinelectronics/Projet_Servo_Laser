#!/usr/bin/python
import BBIO
from time import sleep
import serial
import menu
import wiimote
import threading

sleep(1) #Permet d'attend au démarrage que les dossiers pour les GPIOs sont créés

BBIO.initPWM()
BBIO.initGPIO()
BBIO.initUART()

UART1 = serial.Serial(port="/dev/ttyO1", baudrate=115200, timeout=0)

sleep(1)

def Connexion_OK():
	threading.Timer(1.0, Connexion_OK).start()
	
	if UART1.writable():
		UART1.write('$\n')
		
Connexion_OK()

Rx = "\0"

UART1.flushInput()

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
