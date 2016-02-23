#!/usr/bin/python
import os
from time import sleep

##initPWM()
# Initialise 2 PWM sur P9_14 et P9_22
# T = 20ms
# Th = 1.5ms (servomoteurs a  0degre)
def initPWM():

	os.system("echo am33xx_pwm > /sys/devices/bone_capemgr.9/slots")
	os.system("echo bone_pwm_P9_14 > /sys/devices/bone_capemgr.9/slots")
	os.system("echo bone_pwm_P9_22 > /sys/devices/bone_capemgr.9/slots")

	sleep(2) #Tempo pour attendre la creation des fichiers

	os.system("echo 20000000 > /sys/devices/ocp.3/pwm_test_P9_14.15/period")
	os.system("echo 1500000 > /sys/devices/ocp.3/pwm_test_P9_14.15/duty")
	os.system("echo 20000000 > /sys/devices/ocp.3/pwm_test_P9_22.16/period")
	os.system("echo 1500000 > /sys/devices/ocp.3/pwm_test_P9_22.16/duty")

##initSerial()
#Initialise la liaison serie UART1 sur P9_24(Tx) P9_26(Rx)
#Baudrate = 115200
#8 bits
#1 stop
#pas de parite
def initUART():

	os.system("echo BB-UART1 > /sys/devices/bone_capemgr.9/slots")

	sleep(2) #Tempo pour attendre la creation du fichier

##initGPIO()
#Initialise 3 GPIOs GPIO66(P8_07) GPIO69(P8_09) GPIO45(P8_11)
def initGPIO():

	os.system("echo 66 > /sys/class/gpio/export")
	os.system("echo 69 > /sys/class/gpio/export")
	os.system("echo 45 > /sys/class/gpio/export")

	sleep(2)

	os.system("echo high > /sys/class/gpio/gpio66/direction")
	os.system("echo high > /sys/class/gpio/gpio69/direction")
	os.system("echo high > /sys/class/gpio/gpio45/direction")

	os.system("echo 0 > /sys/class/gpio/gpio66/value")
	os.system("echo 0 > /sys/class/gpio/gpio69/value")
	os.system("echo 0 > /sys/class/gpio/gpio45/value")

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

	os.system("echo " + duty + " > /sys/devices/ocp.3/pwm_test_P9_14.15/duty")

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

	os.system("echo " + duty + " > /sys/devices/ocp.3/pwm_test_P9_22.16/duty")

##laser()
#Active ou desactive le laser
def laser(etat):

	if etat == "on":
		os.system("echo 1 > /sys/class/gpio/gpio45/value")	
	else:
		os.system("echo 0 > /sys/class/gpio/gpio45/value")

##mode()
#Allume une led pour indiquer dans quel mode de fonctionnement se trouve le programme
def mode(MA):

	if MA == 'M':

		os.system("echo 1 > /sys/class/gpio/gpio66/value")
		os.system("echo 0 > /sys/class/gpio/gpio69/value")
	else:
		os.system("echo 0 > /sys/class/gpio/gpio66/value")
		os.system("echo 1 > /sys/class/gpio/gpio69/value")
		
