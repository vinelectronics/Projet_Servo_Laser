#!/usr/bin/python
from time import sleep
import serial
import BBIO
import Affichage
import Commande
import cwiid

##modeMAnuel
#Permet de controler les servomoteurs et le laser manuellement
#incrementation 10degres
def modeManuel(UART1):

	mode = 'm'

	angleSm1 = 0
	angleSm2 = 0
	etatLaser = "off"

	BBIO.servomoteur1(angleSm1)
	BBIO.servomoteur2(angleSm2)
	BBIO.laser(etatLaser)

	BBIO.mode(mode)

	while mode == 'm':

		Affichage.parametres(-angleSm2, angleSm1, etatLaser, "Manuel", UART1)
		rcv = UART1.read()


		if rcv == 'z':
			if angleSm1 < 90:
				angleSm1 += 10
				BBIO.servomoteur1(angleSm1)
		elif rcv == 's':
			if angleSm1 > -90:
				angleSm1 -= 10
				BBIO.servomoteur1(angleSm1)
		elif rcv == 'd':
			if angleSm2 > -90:
				angleSm2 -= 10
				BBIO.servomoteur2(angleSm2)
		elif rcv == 'q':
			if angleSm2 < 90:
				angleSm2 += 10
				BBIO.servomoteur2(angleSm2)
		elif rcv == 'a':
			if etatLaser == "on":
				etatLaser = "off"
			else:
				etatLaser = "on"
			BBIO.laser(etatLaser)
		elif rcv == 'e':
			mode = 'a'
##modeAuto
#mode 0 : carre
#mode 1 : losange
#mode 2 : cercle
def modeAuto(UART1):

	mode = 'a'

	angleSm1 = 0
	angleSm2 = 0
	etatLaser = "off"

	BBIO.servomoteur1(angleSm1)
	BBIO.servomoteur2(angleSm2)
	BBIO.laser(etatLaser)

	BBIO.mode(mode)

	nmode = 0

	while mode == 'a':

		if nmode == 0: 
			Commande.carre(UART1)
			nmode = 1
		elif nmode == 1:
			Commande.losange(UART1)
			nmode = 2
		elif nmode == 2:
			Commande.cercle(UART1)
			mode = 'm'
