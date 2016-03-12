#!/usr/bin/python
import serial
import string
from time import sleep

##affichage()
#Affiche l'angle des servomoteurs
#Affiche l'etat du laser
#affiche le mode manuel ou predefini
def parametres(V, H, Laser, UART1):

	if Laser == 1 : Laser = "ON"
	else: Laser = "OFF"
	
	
	chaine = "#PARAM,%s,%+d,%+d," % (Laser, H, V)
	
	UART1.write(chaine)
	sleep(0.005)
	UART1.flushOutput()
