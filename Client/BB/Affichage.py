#!/usr/bin/python
import serial
import string

##affichage()
#Affiche l'angle des servomoteurs
#Affiche l'etat du laser
#affiche le mode manuel ou predefini
def parametres(V, H, Laser, UART1):

	if Laser == 1 : Laser = "ON"
	else: Laser = "OFF"
	
	chaine = "#PARAM,%s,%+d,%+d\r\n" % (Laser, H, V)

	UART1.write(chaine)
