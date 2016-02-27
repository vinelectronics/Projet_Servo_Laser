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
	y = 20

	BBIO.servomoteur1(x)
	BBIO.servomoteur2(y)

	while UART1.read() != 'r':

		for i in range(20):
			Affichage.parametres(x, y, 'on', 'a', UART1)
			x += 2
			sleep(0.01)
			BBIO.servomoteur1(x)
		
		for i in range(20):
			y -= 2
			sleep(0.01)
			BBIO.servomoteur2(y)

		for i in range(20):
			x -= 2
			sleep(0.01)
			BBIO.servomoteur1(x)

		for i in range(20):
			y += 2
			sleep(0.01)
			BBIO.servomoteur2(y)

	UART1.flushInput()

##losange(UART1)
#@param UART1 pour la liaison serie
#dessine un losange
def losange(UART1):

	BBIO.laser("on")
	x = -20
	y = 0

	BBIO.servomoteur1(x)
	BBIO.servomoteur2(y)

	while UART1.read() != 'r':

		for i in range(10):
			x += 2
			y += 2
			sleep(0.01)
			BBIO.servomoteur1(x)
			BBIO.servomoteur2(y)
		
		for i in range(10):
			x += 2
			y -= 2
			sleep(0.01)
			BBIO.servomoteur1(x)
			BBIO.servomoteur2(y)

		for i in range(10):
			x -= 2
			y -= 2
			sleep(0.01)
			BBIO.servomoteur1(x)
			BBIO.servomoteur2(y)

		for i in range(10):
			x -= 2
			y += 2
			sleep(0.01)
			BBIO.servomoteur1(x)
			BBIO.servomoteur2(y)

	UART1.flushInput()

##cercle(UART1)
#@param UART1 pour la liaison serie
#dessine un cercle
def cercle(UART1):

	BBIO.laser("on")
	x = 20
	y = 0

	BBIO.servomoteur1(x)
	BBIO.servomoteur2(y)


	while UART1.read() != 'r':

		for i in range(0, 79):
			x = int(math.cos(math.radians(360)*i/80.0)*20.0)
			y = int(math.sin(math.radians(360)*i/80.0)*20.0)
			sleep(0.001)
			BBIO.servomoteur1(x)
			BBIO.servomoteur2(y)

	UART1.flushInput()
