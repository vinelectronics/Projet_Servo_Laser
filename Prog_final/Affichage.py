#!/usr/bin/python
import serial
import string

##affichage()
#Affiche l'angle des servomoteurs
#Affiche l'etat du laser
#affiche le mode manuel ou predefini
def parametres(angleSm1, angleSm2, laser, mode, uart1):

	angleSm1 = str(angleSm1)
	angleSm2 = str(angleSm2)
	
	#uart1.write("\033[2J") #efface l'ecran
	uart1.write("\033[H") #retour en position home
	uart1.write("laser = " + laser + "\r\n")
	uart1.write("mode = " + mode + "\r\n")
	uart1.write("Angle servomoteur horizontal : " + angleSm1 + "\r\n")
	uart1.write("Angle servomoteur vertical : " + angleSm2 + "\r\n")
