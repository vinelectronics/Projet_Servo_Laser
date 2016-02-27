#!/usr/bin/python
import cwiid
import time
import BBIO
import Affichage

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




'''
	if wm.state['buttons'] & cwiid.BTN_PLUS:
		wm.rumble = 1
	else: wm.rumble = 0

	if wm.state['buttons'] & cwiid.BTN_A:
		wm.led = (wm.state['led'] + 1) % 16
	time.sleep(.1)
		
	accWX = wm.state['acc'][1]
	accWY = wm.state['acc'][0]
	accWZ = wm.state['acc'][2]
	
	accNX = wm.state['nunchuk']['acc'][cwiid.X]
	accNY = wm.state['nunchuk']['acc'][cwiid.Y]
	accNZ = wm.state['nunchuk']['acc'][cwiid.Z]
'''

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

	time.sleep(1)

	wm.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_ACC | cwiid.RPT_NUNCHUK

	wm.led = 1


	while mode == 'w':
		
		if wm.state['ext_type'] == cwiid.EXT_NUNCHUK:
			
			NunX = -1.0*int((wm.state['nunchuk']['stick'][0] - 28)*(180.0/200.0)-90)
			NunY = int(wm.state['nunchuk']['stick'][1] - 34*(180.0/190.0)-90)
		
			BBIO.servomoteur1(NunY)
			BBIO.servomoteur2(NunX)

			if wm.state['nunchuk']['buttons'] & cwiid.NUNCHUK_BTN_Z:
				etatLaser = 'on'
			else :
				etatLaser = 'off'

			BBIO.laser(etatLaser)
				
			Affichage.parametres(NunX, NunY, etatLaser, mode, UART1)

		elif wm.state['ext_type'] == cwiid.EXT_NONE:

			accWX = int((wm.state['acc'][1] - 96)*(180.0/48.0)-90)
			accWY = -1.0*int((wm.state['acc'][0] - 96)*(180.0/48.0)-90)

			BBIO.servomoteur1(accWY)
			BBIO.servomoteur2(accWX)

			if wm.state['buttons'] & cwiid.BTN_A:
				etatLaser = 'on'
			else :
				etatLaser = 'off'

			BBIO.laser(etatLaser)

			Affichage.parametres(accWX, accWY, etatLaser, mode, UART1)

	#print "Wiimote : AX = %d AY = %d AZ = %d  Nunchuk : AX = %d AY = %d AZ = %d SX = %d SY = %d" %(accWX, accWY, accWZ, accNX, accNY, accNZ, NunX, NunY)

		if wm.state['buttons'] & cwiid.BTN_B:
			wm.close()
			mode = 'e'


