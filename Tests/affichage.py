#!/usr/bin/python
import os
from time import sleep
from threading import Timer,Thread,Event

class perpetualTimer():

   def __init__(self,t,hFunction):
      self.t=t
      self.hFunction = hFunction
      self.thread = Timer(self.t,self.handle_function)

   def handle_function(self):
      self.hFunction()
      self.thread = Timer(self.t,self.handle_function)
      self.thread.start()

   def start(self):
      self.thread.start()

   def cancel(self):
      self.thread.cancel()

class statique():
	digit = 1

def segments(chiffre):

	a = "/sys/class/gpio/gpio66/value"
	b = "/sys/class/gpio/gpio69/value"
	c = "/sys/class/gpio/gpio45/value"
	d = "/sys/class/gpio/gpio23/value"
	e = "/sys/class/gpio/gpio47/value"
	f = "/sys/class/gpio/gpio27/value"
	g = "/sys/class/gpio/gpio22/value"

	if chiffre == 0:
		os.system("echo 1 > " + a + " | echo 1 > " + b + " | echo 1 > " + c + " | echo 1 > " + d + " | echo 1 > " + e + " | echo 1 > " + f + " | echo 0 > " + g)
	elif chiffre == 1:
		os.system("echo 0 > " + a + " | echo 1 > " + b + " | echo 1 > " + c + " | echo 0 > " + d + " | echo 0 > " + e + " | echo 0 > " + f + " | echo 0 > " + g)
	elif chiffre == 2:
		os.system("echo 1 > " + a + " | echo 1 > " + b + " | echo 0 > " + c + " | echo 1 > " + d + " | echo 1 > " + e + " | echo 0 > " + f + " | echo 1 > " + g)
	elif chiffre == 3:
		os.system("echo 1 > " + a + " | echo 1 > " + b + " | echo 1 > " + c + " | echo 1 > " + d + " | echo 0 > " + e + " | echo 0 > " + f + " | echo 1 > " + g)
	elif chiffre == 4:
		os.system("echo 0 > " + a + " | echo 1 > " + b + " | echo 1 > " + c + " | echo 0 > " + d + " | echo 0 > " + e + " | echo 1 > " + f + " | echo 1 > " + g)
	elif chiffre == 5:
		os.system("echo 1 > " + a + " | echo 0 > " + b + " | echo 1 > " + c + " | echo 1 > " + d + " | echo 0 > " + e + " | echo 1 > " + f + " | echo 1 > " + g)
	elif chiffre == 6:
		os.system("echo 1 > " + a + " | echo 0 > " + b + " | echo 1 > " + c + " | echo 1 > " + d + " | echo 1 > " + e + " | echo 1 > " + f + " | echo 1 > " + g)
	elif chiffre == 7:
		os.system("echo 1 > " + a + " | echo 1 > " + b + " | echo 1 > " + c + " | echo 0 > " + d + " | echo 0 > " + e + " | echo 0 > " + f + " | echo 0 > " + g)
	elif chiffre == 8:
		os.system("echo 1 > " + a + " | echo 1 > " + b + " | echo 1 > " + c + " | echo 1 > " + d + " | echo 1 > " + e + " | echo 1 > " + f + " | echo 1 > " + g)
	elif chiffre == 9:
		os.system("echo 1 > " + a + " | echo 1 > " + b + " | echo 1 > " + c + " | echo 1 > " + d + " | echo 0 > " + e + " | echo 1 > " + f + " | echo 1 > " + g)

def mux():

	d1 = "/sys/class/gpio/gpio67/value"
	d2 = "/sys/class/gpio/gpio68/value"	
	d3 = "/sys/class/gpio/gpio44/value"
	d4 = "/sys/class/gpio/gpio26/value"

	if statique. digit < 4:
		statique.digit += 1
	else:
		statique.digit = 1

	if statique.digit == 1:
		os.system("echo 0 > " + d1 + " | echo 1 > " + d2 + " | echo 1 > " + d3 + " | echo 1 > " + d4)
	elif statique.digit == 2:
		os.system("echo 1 > " + d1 + " | echo 0 > " + d2 + " | echo 1 > " + d3 + " | echo 1 > " + d4)
	elif statique.digit == 3:
		os.system("echo 1 > " + d1 + " | echo 1 > " + d2 + " | echo 0 > " + d3 + " | echo 1 > " + d4)
	elif statique.digit == 4:
		os.system("echo 1 > " + d1 + " | echo 1 > " + d2 + " | echo 1 > " + d3 + " | echo 0 > " + d4)

	segments(nb)

os.system("echo 66 > /sys/class/gpio/export")
os.system("echo high > /sys/class/gpio/gpio66/direction")
os.system("echo 69 > /sys/class/gpio/export")
os.system("echo high > /sys/class/gpio/gpio69/direction")
os.system("echo 45 > /sys/class/gpio/export")
os.system("echo high > /sys/class/gpio/gpio45/direction")
os.system("echo 23 > /sys/class/gpio/export")
os.system("echo high > /sys/class/gpio/gpio23/direction")
os.system("echo 47 > /sys/class/gpio/export")
os.system("echo high > /sys/class/gpio/gpio47/direction")
os.system("echo 27 > /sys/class/gpio/export")
os.system("echo high > /sys/class/gpio/gpio27/direction")
os.system("echo 22 > /sys/class/gpio/export")
os.system("echo high > /sys/class/gpio/gpio22/direction")

os.system("echo 67 > /sys/class/gpio/export")
os.system("echo high > /sys/class/gpio/gpio67/direction")
os.system("echo 68 > /sys/class/gpio/export")
os.system("echo high > /sys/class/gpio/gpio68/direction")
os.system("echo 44 > /sys/class/gpio/export")
os.system("echo high > /sys/class/gpio/gpio44/direction")
os.system("echo 26 > /sys/class/gpio/export")
os.system("echo high > /sys/class/gpio/gpio26/direction")

nb = 0
#t = perpetualTimer(0.00001,mux)
#t.start()

while 1:

	os.system("echo 0 > /sys/class/gpio/gpio67/value")
	os.system("echo 1 > /sys/class/gpio/gpio67/value")
