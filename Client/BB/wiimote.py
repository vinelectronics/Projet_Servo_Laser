#!/usr/bin/python
import cwiid
import time
import BBIO
import Affichage
from time import sleep

"""

######### Code des boutons ##########
cwiid.
BTN_RIGHT
BTN_UP
BTN_DOWN
BTN_1
BTN_2
BTN_A
BTN_B
BTN_HOME
BTN_MINUS
BTN_PLUS

######## Code accelerometre #########

accWX : wm.state['acc'][1]
accWY : wm.state['acc'][0]
accWZ : wm.state['acc'][2]

### Code stick, accelero et boutons Nunchuk ###

X : wm.state['nunchuk']['stick'][0]
Y : wm.state['nunchuk']['stick'][1]

accNX : wm.state['nunchuk']['acc'][cwiid.X]
accNY : wm.state['nunchuk']['acc'][cwiid.Y]
accNZ : wm.state['nunchuk']['acc'][cwiid.Z]

##########################

"""

def Wii(UART1):

	NunX = 0
	NunY = 0
	Laser = 0
	Exit = 0

	Rx = "MODE,WII,ON"

	BBIO.laser(Laser)
	BBIO.servomoteur1(NunY)
	BBIO.servomoteur2(-NunX)
	Affichage.parametres(NunX, NunY, Laser, UART1)

	wm = cwiid.Wiimote()
	
	sleep(1)

	UART1.write("#WII,CONNECTE")

	#print 'Connecte'
	wm.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_ACC | cwiid.RPT_NUNCHUK

	wm.led = 1

	while not wm.state['buttons'] and cwiid.BTN_HOME and Exit == 0:
			
		while wm.state['ext_type'] == cwiid.EXT_NUNCHUK:
	
			NunX = -1.0*int((wm.state['nunchuk']['stick'][0] - 28)*(180.0/200.0)-90)
			NunY = int(wm.state['nunchuk']['stick'][1] - 34*(180.0/190.0)-90)
			
			BBIO.servomoteur1(NunY)
			BBIO.servomoteur2(-NunX)
			Affichage.parametres(NunX, NunY, Laser, UART1)

			Rx = UART1.readline()
			
			if wm.state['nunchuk']['buttons'] & cwiid.NUNCHUK_BTN_Z:
				if Laser == 1:
					Laser = 0
				else: Laser = 1
				sleep(0.2)
				BBIO.laser(Laser)

			##Pour sortir de la fonction Wii
			if Rx.find('MODE') != -1:

				if Rx.find('WII') != -1: 
					if Rx.find('OFF') != -1: 
						Exit = 1
						Rx = "MODE,MANU"
				else: Exit = 1
				
			elif Rx.find('EXIT') != -1: Exit = 1

			if (wm.state['buttons'] & cwiid.BTN_HOME):
				Rx = "MODE,MANU"
				Exit = 1
			if Exit == 1: break
						
		while wm.state['ext_type'] == cwiid.EXT_NONE:

			accWX = int((wm.state['acc'][1] - 96)*(180.0/48.0)-90)
			accWY = -1.0*int((wm.state['acc'][0] - 96)*(180.0/48.0)-90)
			
			BBIO.servomoteur1(accWY)
			BBIO.servomoteur2(-accWX)
			Affichage.parametres(accWX, accWY, Laser, UART1)

			Rx = UART1.readline()
			
			if wm.state['buttons'] & cwiid.BTN_A:
				if Laser == 1:
					Laser = 0
				else: Laser = 1
				sleep(0.2)
				BBIO.laser(Laser)
			
			##Pour sortir de la fonction Wii
			if Rx.find('MODE') != -1:
				if Rx.find('WII') != -1: 
					if Rx.find('OFF') != -1: 
						Exit = 1
						Rx = "MODE,MANU"
				else: Exit = 1
				
			elif Rx.find('EXIT') != -1: Exit = 1

			if (wm.state['buttons'] & cwiid.BTN_HOME):
				Rx = "MODE,MANU"
				Exit = 1

			if Exit == 1: break

	UART1.write("#WII,NCONNECTE")
	wm.close()
	return Rx
