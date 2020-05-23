#!/home/dwooten/anaconda3/bin/python3

# This file contains the iss class and its methods

import os

from opennotify.iss import *
from opennotify.update import update_tle

class question():

	def __init__(self):
		"""Standard init function for a python class"""

		self.args = None

		self.data = None

		self.opt = None

		self.version = 1.0

		update_tle()

	def check_input(self, opt, args):
		"""This function checks the user input for correctness"""

		self.opt = opt

		self.args = args

	def respond(self):
		"""This function manages the response to the user query"""
		
		
		if self.opt[0] == "loc":

			self.data = get_location()

		else:

			print("Bad input.\n")


		if self.data:

			print(self.data)

		else:
		
			print("No data.\n")
