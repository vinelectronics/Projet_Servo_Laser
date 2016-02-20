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

X : wm.state['acc'][1]
Y : wm.state['acc'][0]
Z : wm.state['acc'][2]

### Code stick et boutons Nunchuk ###

X : wm.state['nunchuk']['stick'][0]
Y : wm.state['nunchuk']['stick'][1]



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
		
	accX = wm.state['acc'][1]
	accY = wm.state['acc'][0]
	accZ = wm.state['acc'][2]

	NunX = wm.state['nunchuk']['stick'][0]
	NunY = wm.state['nunchuk']['stick'][1]

	print "X = %d Y = %d Z = %d  Nunchuk X = %d Y = %d" %(accX, accY, accZ, NunX, NunY)

	if wm.state['buttons'] == 4:
		wm.close()

