#!/usr/bin/python
import cwiid
import time

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

cwiid.NUNCHUK_BTN_C
cwiid.NUNCHUK_BTN_Z

##########################

"""


print 'Appuyez sur 1+2...'

wm = cwiid.Wiimote()

time.sleep(1)

wm.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_ACC | cwiid.RPT_NUNCHUK

wm.led = 1

while True:

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

	NunX = wm.state['nunchuk']['stick'][0]
	NunY = wm.state['nunchuk']['stick'][1]

	print "Wiimote : AX = %d AY = %d AZ = %d  Nunchuk : AX = %d AY = %d AZ = %d SX = %d SY = %d" %(accWX, accWY, accWZ, accNX, accNY, accNZ, NunX, NunY)

	if wm.state['buttons'] == 4:
		wm.close()

