#!/usr/bin/python
from time import sleep
import serial
import BBIO
import math
import Affichage

##carre(UART1)
#@param UART1 pour la liaison serie
#dessine un carre
def carre(UART1):

	BBIO.laser("on")
	x = -20
	y = -20

	BBIO.servomoteur1(x)
	BBIO.servomoteur2(y)

	exit = 0

	while exit == 0:

		Affichage.parametres(x, y, "On", "Automatique : carre", UART1)

		if(x == -20 and y < 20):
			 y += 2
		elif(x < 20 and y == 20):
			 x += 2
		elif(x == 20 and y > -20):
			 y -= 2
		elif(x > -20 and y == -20):
			 x -= 2

		BBIO.servomoteur1(x)
		BBIO.servomoteur2(y)

		sleep(0.05)

		mode = UART1.read()

		if(mode == 'r' or mode == 'p'):
				exit = 1

	UART1.flushInput()

	return mode

##losange(UART1)
#@param UART1 pour la liaison serie
#dessine un losange
def losange(UART1):

	BBIO.laser("on")
	x = -20
	y = 0

	BBIO.servomoteur1(x)
	BBIO.servomoteur2(y)

	exit = 0

	while exit == 0:

		Affichage.parametres(x, y, "On", "Automatique : losange", UART1)
		
		if(x < 0 and y < 20 and y >= 0 ):
			x += 2
			y += 2
		elif(x < 20 and x >= 0 and y > 0):
			x += 2
			y -= 2
		elif(x > 0 and y > -20 and y <= 0):
			x -= 2
			y -= 2
		elif(x > -20 and x <= 0 and y < 0):
			x -= 2
			y += 2

		BBIO.servomoteur1(x)
		BBIO.servomoteur2(y)

		sleep(0.05)

		mode = UART1.read()

		if(mode == 'r' or mode == 'p'):
				exit = 1

	UART1.flushInput()

	return mode

##cercle(UART1)
#@param UART1 pour la liaison serie
#dessine un cercle
def cercle(UART1):

	BBIO.laser("on")
	x = 20
	y = 0

	BBIO.servomoteur1(x)
	BBIO.servomoteur2(y)

	exit = 0

	while exit == 0:

		for i in range(0, 79):

			Affichage.parametres(x, y, "On", "Automatique : cercle", UART1)

			x = int(math.cos(math.radians(360)*i/80.0)*20.0)
			y = int(math.sin(math.radians(360)*i/80.0)*20.0)
			sleep(0.01)
			BBIO.servomoteur1(x)
			BBIO.servomoteur2(y)

			mode = UART1.read()

			if(mode == 'r' or mode == 'p'):
				exit = 1

	UART1.flushInput()

	return mode
