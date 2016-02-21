#!/usr/bin/python
#import string
import os
from time import sleep

def position(SM1):

	SM1 += 90
	SM1 /= 180
	SM1 *= 1000000
	SM1 += 1000000

	SM1 = int(SM1)

	duty = str(SM1)

	com = "echo " + duty + " > /sys/devices/ocp.2/pwm_test_P9_14.9/duty"
	os.system(com)

os.system("echo am33xx_pwm > /sys/devices/bone_capemgr.7/slots")
os.system("echo bone_pwm_P9_14 > /sys/devices/bone_capemgr.7/slots")
os.system("echo 20000000 > /sys/devices/ocp.2/pwm_test_P9_14.9/period")
os.system("echo 10000000 > /sys/devices/ocp.2/pwm_test_P9_14.9/duty")

periode = "20000000"
angle = 0.0
polarite = "0"
d = 1
nbPas = 180
unitAngle = (180.0/nbPas)

com = "echo " + periode + " > /sys/devices/ocp.2/pwm_test_P9_14.9/period"
os.system(com)

com = "echo " + polarite + " > /sys/devices/ocp.2/pwm_test_P9_14.9/polarity"
os.system(com)

while 1:

	sleep(0.01)
	
	if d == 1:

		if(angle >= 90):
			d = 0
		angle += unitAngle

	else:

		if(angle <= -90):
			d = 1
		angle -= unitAngle	

	position(angle)
