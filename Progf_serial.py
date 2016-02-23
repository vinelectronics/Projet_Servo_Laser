#!/usr/bin/python
import os
from time import sleep
import serial
import string
import math

##initPWM()
# Initialise 2 PWM sur P9_14 et P9_22
# T = 20ms
# Th = 1.5ms (servomoteurs a  0degre)
def initPWM():

	os.system("echo am33xx_pwm > /sys/devices/bone_capemgr.7/slots")
	os.system("echo bone_pwm_P9_14 > /sys/devices/bone_capemgr.7/slots")
	os.system("echo bone_pwm_P9_22 > /sys/devices/bone_capemgr.7/slots")

	sleep(2) #Tempo pour attendre la creation des fichiers

	os.system("echo 20000000 > /sys/devices/ocp.2/pwm_test_P9_14.9/period")
	os.system("echo 1500000 > /sys/devices/ocp.2/pwm_test_P9_14.9/duty")
	os.system("echo 20000000 > /sys/devices/ocp.2/pwm_test_P9_22.10/period")
	os.system("echo 1500000 > /sys/devices/ocp.2/pwm_test_P9_22.10/duty")

##initSerial()
#Initialise la liaison serie UART1 sur P9_24(Tx) P9_26(Rx)
#Baudrate = 115200
#8 bits
#1 stop
#pas de parite
def initSerial():

	os.system("echo BB-UART1 > /sys/devices/bone_capemgr.7/slots")

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

##affichage()
#Affiche l'etat du systeme
#@param angleSm1 angle du servomoteur 1
#@param angleSm2 angle du servomoteur 2
#@param laser etat du laser
#@param mode manuel ou auto
#@param uart1 pour envoi des informations sur l'uart
def affichage(angleSm1, angleSm2, laser, mode, uart1):

	angleSm1 = str(angleSm1)
	angleSm2 = str(angleSm2)
	
	#uart1.write("\033[2J") #efface l'ecran
	uart1.write("\033[H") #retour en position home
	uart1.write("laser = " + laser + "\r\n")
	uart1.write("mode = " + mode + "\r\n")
	uart1.write("Angle servomoteur horizontal : " + angleSm1 + "\r\n")
	uart1.write("Angle servomoteur vertical : " + angleSm2 + "\r\n")

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

	os.system("echo " + duty + " > /sys/devices/ocp.2/pwm_test_P9_14.9/duty")

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

	os.system("echo " + duty + " > /sys/devices/ocp.2/pwm_test_P9_22.10/duty")

##laser()
#Active ou desactive le laser
def laser(etat):

	if etat == "on":
		os.system("echo 1 > /sys/class/gpio/gpio45/value")	
	else:
		os.system("echo 0 > /sys/class/gpio/gpio45/value")

##carre(UART1)
#dessine un carre avec un angle -20<angle<20
def carre(UART1):

	laser("on")
	x = -20
	y = 20

	servomoteur1(x)
	servomoteur2(y)

	while UART1.read() != 'r':

		for i in range(10):
			x += 4
			sleep(0.001)
			servomoteur1(x)
		
		for i in range(10):
			y -= 4
			sleep(0.001)
			servomoteur2(y)

		for i in range(10):
			x -= 4
			sleep(0.001)
			servomoteur1(x)

		for i in range(10):
			y += 4
			sleep(0.001)
			servomoteur2(y)

	UART1.flushInput()

##losange(UART1)
#Dessine un losange avec un angle -20<angle<20
def losange(UART1):

	laser("on")
	x = -20
	y = 0

	servomoteur1(x)
	servomoteur2(y)

	while UART1.read() != 'r':

		for i in range(10):
			x += 4
			y += 4
			sleep(0.001)
			servomoteur1(x)
			servomoteur2(y)
		
		for i in range(10):
			x += 4
			y -= 4
			sleep(0.001)
			servomoteur1(x)
			servomoteur2(y)

		for i in range(10):
			x -= 4
			y -= 4
			sleep(0.001)
			servomoteur1(x)
			servomoteur2(y)

		for i in range(10):
			x -= 4
			y += 4
			sleep(0.001)
			servomoteur1(x)
			servomoteur2(y)

	UART1.flushInput()

##cercle(UART1)
#Dessine un cercle avec un angle -20<angle<20
def cercle(UART1):

	laser("on")
	x = 20
	y = 0

	servomoteur1(x)
	servomoteur2(y)


	while UART1.read() != 'r':

		for i in range(40):
			x = int(math.cos((2*3.14)/(40-i))*20.0)
			y = int(math.sin((2*3.14)/(40-i))*20.0)
			sleep(0.001)
			servomoteur1(x)
			servomoteur2(y)

	UART1.flushInput()

##modeMAnuel
#Permet de controler les servomoteurs et le laser manuellement
#incrementation 10degres
def modeManuel(angleSm1, angleSm2, mode, etatLaser, UART1):

	servomoteur1(0)
	servomoteur2(0)
	laser(0)

	while mode == 'm':

		affichage(angleSm1, angleSm2, etatLaser, mode, UART1)
		rcv = UART1.read()

		if rcv == 'z':
			if angleSm1 < 90:
				angleSm1 += 10
				servomoteur1(angleSm1)
		elif rcv == 's':
			if angleSm1 > -90:
				angleSm1 -= 10
				servomoteur1(angleSm1)
		elif rcv == 'q':
			if angleSm2 > -90:
				angleSm2 -= 10
				servomoteur2(angleSm2)
		elif rcv == 'd':
			if angleSm2 < 90:
				angleSm2 += 10
				servomoteur2(angleSm2)
		elif rcv == 'a':
			if etatLaser == "on":
				etatLaser = "off"
			else:
				etatLaser = "on"
			laser(etatLaser)
		elif rcv == 'e':
			mode = 'a'
##modeAuto
#mode 0 : carre
#mode 1 : losange
#mode 2 : cercle
def modeAuto(angleSm1, angleSm2, mode, etatLaser, UART1):

	servomoteur1(0)
	servomoteur2(0)
	laser(0)

	nmode = 0

	while mode == 'a':

		affichage(angleSm1, angleSm2, etatLaser, mode, UART1)
		sleep(0.1)
		rcv = UART1.read()

		if rcv == 'e':
			mode = 'm'

		if nmode == 0: 
			carre(UART1)
			nmode = 1
		elif nmode == 1: losange(UART1)
		elif nmode == 2: cercle(UART1)

##Programme principal
print "Initialisations des perihperiques en cours..."

initPWM()
initSerial()
initGPIO()

etatLaser = "off"
mode = 'm'
angleSm1 = 0
angleSm2 = 0

UART1 = serial.Serial(port="/dev/ttyO1", baudrate=115200, timeout=0)

print "Peripheriques initialises"

sleep(1)

while True:

	if mode == 'm':
		modeManuel(angleSm1, angleSm2, mode, etatLaser, UART1)
		mode = 'a'
	else:
		modeAuto(angleSm1, angleSm2, mode, etatLaser, UART1)
		mode = 'm'
