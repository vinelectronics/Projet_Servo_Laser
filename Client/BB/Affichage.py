#!/usr/bin/python
import serial
import string

##affichage()
#Affiche l'angle des servomoteurs
#Affiche l'etat du laser
#affiche le mode manuel ou predefini
def parametres(V, H, Laser, UART1):

	V = str(V)
	H = str(H)

	CR = 0x0D
	LF = 0x0A

	if Laser == 1 : Laser = "ON"
	else: Laser = "OFF"
	
	UART1.write("#PARAM," + Laser + "," + H + ',' + V + CR + LF)
