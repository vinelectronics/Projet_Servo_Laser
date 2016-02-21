#!/usr/bin/python
from time import sleep
import os
import sys
import select
import tty
import termios

class NonBlockingConsole(object):

	def __enter__(self):
		self.old_settings = termios.tcgetattr(sys.stdin)
		tty.setcbreak(sys.stdin.fileno())
		return self

	def __exit__(self, type, value, traceback):
		termios.tcsetattr(sys.stdin, termios.TCSADRAIN, self.old_settings)

	def get_data(self):
		if select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], []):
			return sys.stdin.read(1)
		return False

with NonBlockingConsole() as nbc:

	i = 0
	inc = 0

	while 1:

		os.system("clear")
		print i
	
		if inc == 0:
			i += 1
		else:
			i -= 1	

		for n in range(0, 100):
			n = nbc.get_data()
			if n == '0':
				inc = 0;
			elif n == '1':
				inc = 1;
			sleep(0.01)
