#!/home/dwooten/anaconda3/bin/python3

# This file contains the iss class and its methods

import os
import urllib
import json
import math
from datetime import datetime, timezone

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

			print("Error: First command line argument, {}, is not of type string.\n Acceptable command line arguments following the invocation of the executable include and are limited to...\n1. loc\n2. pass\n3. people\n".format(opt))

			self.exit = 1

			return

# Following assurances of type string, check that opt is an acceptable choice

		if opt not in ["loc", "pass", "people"]:

			print("Error: First command line argument, {}, is not an acceptable option.\n Acceptable command line arguments following the invocation of the executable include and are limited to...\n1. loc\n2. pass\n3. people\n".format(opt))

			self.exit = 1

			return

# Having verified that opt is good, set opt

		self.opt = opt

# Now that opt has been set, if opt requires additional arguments, check them

		if self.opt == "pass":

			self.check_pass_arguments(args)

	def check_pass_arguments(self, args):
		"""This funtion checks that arguments passed for the "pass"
	        command line option are of valid type and range."""

# Pass requires a latitude and a longtitude coordinate pair, if there are not
# at least 2 entries following the argument 'pass', the input is insufficient

		if len(args) < 2:

			print("Error: Command line argument 'pass' requires two additional command line arguments, both floating point numbers, following itself. These numbers are, respectively, the latitude and longitude of the position over which it is desired to know when the ISS will pass overhead.\n")

			self.exit = 1

			return

# Attempt to convert the latitude input to a float value

		try:

			lat = float(args[0])

		except ValueError:

			print("Error: First command line argument, {}, given following the command line argument of 'pass', is of bad type and can not be converted to a floating point type. Please try again with a second command line argument of type float.\n".format(args[0]))

			self.exit = 1

			return

# Attempt to convert the longitude input to a float value

		try:

			lon = float(args[1])

		except ValueError:

			print("Error: Second command line argument, {}, given following the command line argument of 'pass {}', is of bad type and can not be converted to a floating point type. Please try again with a third command line argument of type float.\n".format(args[1], lat))

			self.exit = 1

			return

# Check that latitude is within bounds

		if lat < -90.0 or lat > 90.0:

			print("Error: Latitude, {}, is out of bounds. Acceptable values for latitude range [-90, 90].\n".format(lat))

			self.exit = 1

			return

# Check that longitude is within bounds

		if lon < -180.0 or lon > 180.0:

			print("Error: Longitude, {}, is out of bounds. Acceptable values for latitude range [-180, 180].\n".format(lon))

			self.exit = 1

			return

# If the arguments are good, set them

		self.lat = lat

		self.lon = lon

	def get_people(self):
		"""This function pulls the current crew roster for the ISS off
		of Open-Notify's website as their API has hard codded values"""

# Pull the most recent crew roster from the web

		data = json.loads(urllib.request.urlopen("http://api.open-notify.org/astros.json").read())

# Extract the list of people and save that

		self.data = data['people']

	def respond(self):
		"""This function manages the response to the user query"""
		
# If the request was for the current location of the ISS, collect and report
# get_location is method from the Open-Notify-API

		if self.opt  == "loc":

			self.data = get_location()

			print("The ISS's current location at {} UTC is ({:.4f}, {:.4f}).\n".format(datetime.datetime.now().replace(tzinfo=timezone.utc), self.data['iss_position']['latitude'],
			      self.data['iss_position']['longitude']))

# If the request was for the people aboard, get that data and report

		if self.opt == "people":

			self.get_people()

			if self.data is not None:
				
				print("The people currently in space are...\n")

				for person in self.data:

					print("\nName: {}\nCraft: {}\n".format(person['name'], person['craft']))

			else:

				print("Error: Unable to retrieve personel list for the ISS. Please check your internet connection and try again.\n")

		if self.opt == "pass":

# If the request was for when the ISS might pass over a particular location,
# get that data and respond
# get_passes is also a method from the Open-Notify-API. On ValueError is sends
# its own error message when the ISS remains below the horizon. Rather than exit
# on an error, I gracefully catch this and tell the user

			try:

				self.data = get_passes(self.lon, self.lat, 0, 1)

				if self.data is not None:

					minutes = int(self.data['response'][0]['duration'] / 60)

					seconds = self.data['response'][0]['duration'] - minutes * 60

					date = datetime.datetime.fromtimestamp(self.data['request']['datetime'])
					print("The ISS will be overhead ({}, {}) at {} UTC for {} minutes and {} seconds.\n".format(self.lat, self.lon, date, minutes, seconds)) 

			except ValueError:

				print("Error: ISS does not pass over the coordinates ({}, {}).\n".format(self.lat, self.lon))