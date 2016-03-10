#!/usr/bin/python
import BBIO
from time import sleep
import serial
import re
import Affichage
import math

def MANUEL(UART1):

	H = 0
	V = 0
	Laser = 0
	Exit = 0

	Rx = "MODE,MANU"

	BBIO.laser(Laser)
	BBIO.servomoteur1(H)
	BBIO.servomoteur2(V)
	Affichage.parametres(V, H, Laser, UART1)

	while Exit == 0:

		Rx = UART1.readline()

		if Rx.find('COORDONNEE') != -1:

			if Rx.find('H') != -1:

				if Rx.find('POS') != -1:
					if Rx.find('-') != -1:
						H = -1*int(re.findall('\d+', Rx)[0])
					elif Rx.find('+') != -1: 
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
					if Rx.find('-') != -1:
						V = -1*int(re.findall('\d+', Rx)[0])
					elif Rx.find('+') != -1: 
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

			if Rx.find('MANU') == -1: Exit = 1
		elif Rx.find('EXIT') != -1: Exit = 1

	return Rx

##carre(UART1)
#@param UART1 pour la liaison serie
#dessine un carre
def CARRE(UART1):

	H = -20
	V = -20
	Laser = 1
	Exit = 0

	Rx = "MODE,CARRE"

	BBIO.laser(Laser)
	BBIO.servomoteur1(H)
	BBIO.servomoteur2(V)
	Affichage.parametres(V, H, Laser, UART1)

	while Exit == 0:

		Rx = UART1.readline()

		Affichage.parametres(H, V, Laser, UART1)

		if(H == -20 and V < 20):
			 V += 2
		elif(H < 20 and V == 20):
			 H += 2
		elif(H == 20 and V > -20):
			 V -= 2
		elif(H > -20 and V == -20):
			 H -= 2

		BBIO.servomoteur1(H)
		BBIO.servomoteur2(V)

		sleep(0.05)

		if Rx.find('MODE') != -1:

			if Rx.find('CARRE') == -1: Exit = 1
		elif Rx.find('EXIT') != -1: Exit = 1

	return Rx

##losange(UART1)
#@param UART1 pour la liaison serie
#dessine un losange
def LOSANGE(UART1):

	H = -20
	V = 0
	Laser = 1
	Exit = 0

	Rx = "MODE,LOSANGE"

	BBIO.laser(Laser)
	BBIO.servomoteur1(H)
	BBIO.servomoteur2(V)
	Affichage.parametres(V, H, Laser, UART1)

	while Exit == 0:

		Rx = UART1.readline()

		Affichage.parametres(H, V, Laser, UART1)
		
		if(H < 0 and V < 20 and V >= 0 ):
			H += 2
			V += 2
		elif(H < 20 and H >= 0 and V > 0):
			H += 2
			V -= 2
		elif(H > 0 and V > -20 and V <= 0):
			H -= 2
			V -= 2
		elif(H > -20 and H <= 0 and V < 0):
			H -= 2
			V += 2

		BBIO.servomoteur1(H)
		BBIO.servomoteur2(V)

		sleep(0.05)

		mode = UART1.read()

		if Rx.find('MODE') != -1:

			if Rx.find('LOSANGE') == -1: Exit = 1
		elif Rx.find('EXIT') != -1: Exit = 1

	return Rx

##cercle(UART1)
#@param UART1 pour la liaison serie
#dessine un cercle
def CERCLE(UART1):

	H = 20
	V = 0
	Laser = 1
	Exit = 0

	Rx = "MODE,CERCLE"

	BBIO.laser(Laser)
	BBIO.servomoteur1(H)
	BBIO.servomoteur2(V)
	Affichage.parametres(V, H, Laser, UART1)

	while Exit == 0:

		for i in range(0, 79):

			Rx = UART1.readline()

			Affichage.parametres(H, V, Laser, UART1)

			H = int(math.cos(math.radians(360)*i/80.0)*20.0)
			V = int(math.sin(math.radians(360)*i/80.0)*20.0)
			sleep(0.01)
			BBIO.servomoteur1(H)
			BBIO.servomoteur2(V)

			if Rx.find('MODE') != -1:

				if Rx.find('CERCLE') == -1:
					Exit = 1
					break
			elif Rx.find('EXIT') != -1:
				Exit = 1
				break
	return Rx
