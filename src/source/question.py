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

		self.exit = 0

		self.lat = None

		self.lon = None

		self.opt = None

		self.version = 1.0

		update_tle()

	def check_input(self, opt, args):
		"""This function checks the user input for correctness"""

# First, ensure that the opt argument is of type string

		if type(opt) is not str:

			print("Error: First command line argument, {}, is not of type string.\n Acceptable command line arguments following the invocation of the executable include and are limited to...\n1. loc\n2. pass\n3. people.\n".format(opt))

			self.exit = 1

			return

# Following assurances of type string, check that opt is an acceptable choice

		if opt is not in ["loc", "pass", "people"]:

			print("Error: First command line argument, {}, is not an acceptable option.\n Acceptable command line arguments following the invocation of the executable include and are limited to...\n1. loc\n2. pass\n3. people.\n".format(opt))

			self.exit = 1

			return

# Having verified that opt is good, set opt

		self.opt = opt

# Now that opt has been set, if opt requires additional arguments, check them

		if self.opt == "pass":

			self.check_pass_arguments(args)

	def check_pass_arguments(Self, args):
		"""This funtion checks that arguments passed for the "pass"
	        command line option are of valid type and range."""

# Pass requires a latitude and a longtitude coordinate pair, if there are not
# at least 2 entries following the argument 'pass', the input is insufficient

		if len(args) < 2:

			print("Error: Command line argument 'pass' requires two additional command line arguments, both floating point numbers, following itself. These numbers are, respectively, the latitude and longitude of the position over which it is desired to know when the ISS will pass overhead.\n")

# Attempt to convert the latitude input to a float value

		try:

			lat = float(args[0])

		except TypeError:

			print("Error: First command line argument, {}, given following the command line argument of 'pass', is of bad type and can not be converted to a floating point type. Please try again with a second command line argument of type float.\n".format(args[0]))

			self.exit = 1

			return

# Attempt to convert the longitude input to a float value

		try:

			lon = float(args[1])

		except TypeError:

			print("Error: Second command line argument, {}, given following the command line argument of 'pass {}', is of bad type and can not be converted to a floating point type. Please try again with a third command line argument of type float.\n".format(args[1], lat))

			self.exit = 1

			return

# Check that latitude is within bounds

		if lat < -90.0 or lat > 90.0:

			print("Error: Latitude, {}, is out of bounds. Acceptable values for latitude range [-90, 90].\n".format(lat))

			self.exit = 1

			return

# Check that longitude is within bounds

		if lon < -180.0 or lat > 180.0:

			print("Error: Longitude, {}, is out of bounds. Acceptable values for latitude range [-180, 180].\n".format(lat))

			self.exit = 1

			return

# If the arguments are good, set them

		self.lat = lat

		self.lon = lon

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
