#!/usr/bin/python
import string
import os

class PWM():

	def __init__(self, pin):
		self.pin = pin
		self.frequence = 50
		self.periode = 20000000
		self.duty = 0.1
		self.polarite = 0

	def setfrequence(self, f):
		
		self.frequence = f
		self.periode = 1000000 / self.frequence
		p = 1/f
		p = p * 1000000
		p = str(p)
		os.system("echo " + p + " > /sys/devices/ocp.2/pwm_test_" + self.pin + ".*/period")

	def setpolarite(self, p):

		self.polarite = p
		p = str(p)
		os.system("echo " + p + " > /sys/devices/ocp.2/pwm_test_" + self.pin + ".*/polarity")

	def setduty(self, d):

		self.duty = d
		dd = d * self.periode
		dd = str(dd)
		os.system("echo " + dd + " > /sys/devices/ocp.2/pwm_test_" + self.pin + ".*/duty")

	def parametre(self, f = self.frequence, d = self.duty, p = self.polarite):

		os.system("echo am33xx_pwm > /sys/devices/bone_capemgr.*/slots")
		os.system("echo bone_pwm_" + self.pin + " > /sys/devices/bone_capemgr.*/slots")
		setfrequence(f)
		setduty(d)
		setpolarite(p)

a = PWM("P9_14")
a.parametre(50, 0.1, 0)
