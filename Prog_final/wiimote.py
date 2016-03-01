#!/usr/bin/python
import cwiid
import time
import BBIO
import Affichage
from time import sleep

"""

############### Code des boutons ##############
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

############ Code accelerometre ###############

accWX : wm.state['acc'][1]
accWY : wm.state['acc'][0]
accWZ : wm.state['acc'][2]

### Code stick, accelero et boutons Nunchuk ###

X : wm.state['nunchuk']['stick'][0]
Y : wm.state['nunchuk']['stick'][1]

accNX : wm.state['nunchuk']['acc'][cwiid.X]
accNY : wm.state['nunchuk']['acc'][cwiid.Y]
accNZ : wm.state['nunchuk']['acc'][cwiid.Z]

###############################################

"""

def Wii(UART1):
	mode = 'w'

	angleSm1 = 0
	angleSm2 = 0
	etatLaser = "off"

	BBIO.servomoteur1(angleSm1)
	BBIO.servomoteur2(angleSm2)
	BBIO.laser(etatLaser)

	BBIO.mode(mode)

	print 'Appuyez sur 1+2...'

	wm = cwiid.Wiimote()

	sleep(1)

	wm.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_ACC | cwiid.RPT_NUNCHUK

	wm.led = 1

	while mode == 'w':
	
		while wm.state['ext_type'] == cwiid.EXT_NUNCHUK: ## Tant que le Nunchuk est branché
	
			NunX = -1.0*int((wm.state['nunchuk']['stick'][0] - 28)*(180.0/200.0)-90) # Convertion des données du stick du Nunchuk en un angle compris entre -90 et 90
			NunY = int(wm.state['nunchuk']['stick'][1] - 34*(180.0/190.0)-90)        #
			
			BBIO.servomoteur1(NunY)
			BBIO.servomoteur2(NunX)
			
			Affichage.parametres(NunX, NunY, etatLaser, mode, UART1)
			
			## Allume ou éteint le laser lorsque l'on appuie sur le bouton 'Z' du Nunchuk
			if wm.state['nunchuk']['buttons'] & cwiid.NUNCHUK_BTN_Z:
				if etatLaser == "on":
					etatLaser = "off"
				else: etatLaser = "on"
				sleep(0.2)
				BBIO.laser(etatLaser)
			
			## Deconnecte la mannette lors de l'appuie de la touche 'home'
			if wm.state['buttons'] & cwiid.BTN_HOME:
				wm.close()
				mode = 'e'
				
		while wm.state['ext_type'] == cwiid.EXT_NONE: ## Tant que le Nunchuk est débranché

			accWX = int((wm.state['acc'][1] - 96)*(180.0/48.0)-90)      # Convertion des données de l'accelero de la manette en un angle compris entre -90 et 90
			accWY = -1.0*int((wm.state['acc'][0] - 96)*(180.0/48.0)-90) #
			
			BBIO.servomoteur1(accWY)
			BBIO.servomoteur2(accWX)
			
			Affichage.parametres(accWX, accWY, etatLaser, mode, UART1)
			
			## Allume ou éteint le laser lorsque l'on appuie sur le bouton 'A' de la manette
			if wm.state['buttons'] & cwiid.BTN_A:
				if etatLaser == "on":
					etatLaser = "off"
				else: etatLaser = "on"
				sleep(0.2)
				BBIO.laser(etatLaser)
				
			## Deconnecte la mannette lors de l'appuie de la touche 'home'
			if wm.state['buttons'] & cwiid.BTN_HOME:
				wm.close()
				mode = 'e'
