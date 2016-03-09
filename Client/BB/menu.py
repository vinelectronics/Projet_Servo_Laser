#!/usr/bin/python
import BBIO
from time import sleep
import serial
import re
import Affichage

def MANUEL(UART1):

	H = 0
	V = 0
	Laser = 0
	Exit = 0

	Rx = "MODE,MANU"

	while Exit == 0:

		Rx = UART1.readline()

		if Rx.find('COORDONNEE') != -1:

			if Rx.find('H') != -1:

				if Rx.find('POS') != -1:
					H = int(re.findall('\d+', Rx)[0])
				elif Rx.find('ADD') != -1:

					if Rx.find('-') != -1:
						H = H - int(re.findall('\d+', Rx)[0])
					elif Rx.find('+') != -1:
						H = H + int(re.findall('\d+', Rx)[0])

					if H > 90: H = 90
					elif H < -90: H = -90

			elif Rx.find('V') != -1:

				if Rx.find('POS') != -1:
					V = int(re.findall('\d+', Rx)[0])
				elif Rx.find('ADD') != -1:

					if Rx.find('-') != -1:
						V = V - int(re.findall('\d+', Rx)[0])
					elif Rx.find('+') != -1:
						V = V + int(re.findall('\d+', Rx)[0])

					if V > 90: V = 90
					elif V < -90: V = -90

			UART1.flushInput()

			BBIO.servomoteur1(H)
			BBIO.servomoteur2(V)
			Affichage.parametres(V, H, Laser, UART1)
		elif Rx.find('LASER') != -1:

			if Rx.find('ON') != -1: Laser = 1
			elif Rx.find('OFF') != -1: Laser = 0

			UART1.flushInput()

			BBIO.laser(Laser)
			Affichage.parametres(V, H, Laser, UART1)
		elif Rx.find('MODE') != -1:

			if Rx.find('CARRE') == -1: Exit = 1
		elif Rx.find('EXIT') != -1: Exit = 1

	return Rx
