#!/usr/bin/python
import os
from time import sleep

##FileWrite(valeur, chemin, TypeOuverture)
# Ecrit 'valeur' dans le fichier ce trouvant dans 'chemin'
# TypeOuverture, 'w' = effacer et ecrire, 'a' = ecrire a la suite

def FileWrite(valeur, chemin, TypeOuverture):

	fichier = open(chemin, TypeOuverture)
	
	fichier.write(valeur)
	
	#fichier.close()

##initPWM()
# Initialise 2 PWM sur P9_14 et P9_22
# T = 20ms
# Th = 1.5ms (servomoteurs a  0degre)

def initPWM():
	
	FileWrite("am33xx_pwm", "/sys/devices/bone_capemgr.9/slots", "a")
	FileWrite("bone_pwm_P9_14", "/sys/devices/bone_capemgr.9/slots", "a")
	FileWrite("bone_pwm_P9_22", "/sys/devices/bone_capemgr.9/slots", "a")
	
	sleep(1) #Tempo pour attendre la creation des fichiers
	
	FileWrite("20000000", "/sys/devices/ocp.3/pwm_test_P9_14.15/period", "w")
	FileWrite("1500000", "/sys/devices/ocp.3/pwm_test_P9_14.15/duty", "w")
	FileWrite("20000000", "/sys/devices/ocp.3/pwm_test_P9_22.16/period", "w")
	FileWrite("1500000", "/sys/devices/ocp.3/pwm_test_P9_22.16/duty", "w")


##initSerial()
#Initialise la liaison serie UART1 sur P9_24(Tx) P9_26(Rx)
#Baudrate = 115200
#8 bits
#1 stop
#pas de parite

def initUART():

	FileWrite("BB-UART1", "/sys/devices/bone_capemgr.9/slots", "a")

	sleep(1) #Tempo pour attendre la creation du fichier


##initGPIO()
#Initialise 3 GPIOs GPIO66(P8_07) GPIO69(P8_09) GPIO45(P8_11)

def initGPIO():

	FileWrite("66", "/sys/class/gpio/export", "a")
	FileWrite("69", "/sys/class/gpio/export", "a")
	FileWrite("45", "/sys/class/gpio/export", "a")

	sleep(1)

	FileWrite("high", "/sys/class/gpio/gpio66/direction", "w")
	FileWrite("high", "/sys/class/gpio/gpio69/direction", "w")
	FileWrite("high", "/sys/class/gpio/gpio45/direction", "w")

	FileWrite("0", "/sys/class/gpio/gpio66/value", "w")
	FileWrite("0", "/sys/class/gpio/gpio69/value", "w")
	FileWrite("0", "/sys/class/gpio/gpio45/value", "w")


##servomoteur1()
#Controle le servomoteur 1
#parametre entree : -90<angle<+90

def servomoteur1(angle):

	angle += 90
	angle /= 180.0
	duty = angle * 1000000.0
	duty += 1000000
	duty = int(duty)
	duty = str(duty)

	FileWrite(duty, "/sys/devices/ocp.3/pwm_test_P9_14.15/duty", "w")


##servomoteur2()
#Controle le servomoteur 2
#parametre entree : -90<angle<+90

def servomoteur2(angle):

	angle += 90
	angle /= 180.0
	duty = angle * 1000000.0
	duty += 1000000
	duty = int(duty)
	duty = str(duty)

	FileWrite(duty, "/sys/devices/ocp.3/pwm_test_P9_22.16/duty", "w")

##laser()
#Active ou desactive le laser
def laser(etat):

	if etat == "on":
		FileWrite("1", "/sys/class/gpio/gpio45/value", "w")	
	else:
		FileWrite("0", "/sys/class/gpio/gpio45/value", "w")

##mode()
#Allume une led pour indiquer dans quel mode de fonctionnement se trouve le programme
def mode(MA):

	if MA == 'm':
		FileWrite("1", "/sys/class/gpio/gpio66/value", "w")
		FileWrite("0", "/sys/class/gpio/gpio69/value", "w")
	else:
		FileWrite("0", "/sys/class/gpio/gpio66/value", "w")
		FileWrite("1", "/sys/class/gpio/gpio69/value", "w")
		
