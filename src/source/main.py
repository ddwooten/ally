#!/home/dwooten/anaconda3/bin/python

## @package iss_check_status_engine
# This file and its associated methods comprise the iss_check_status_engine.
#
# Author: Daniel Wooten
# Date: 05/22/2020
# Version: 1.0
#
# This is the executing program for the data challenge - this function is what
# you run in the command line

import sys 

from question import question


def main():
	"""Iss check status engine. 
		
	This function, when executed from the command line with the appropriate
	arguments will retrieve from the web and display certain informations
	pertaining to the ISS.
	
	For more detailed notes on usage, please see the user manual located
	two levels up the directory and inside of the docs/ subdirectory.
	
	The command line invocation for this function requires at least one
	variable command line argument and up to three depending on choices
	made by the user.
	
	Command line options and their resulting behavior are described below.
	
	1. 'loc' - provides the current location of the ISS in
	(latitude, longitude)
	
	2. 'people' - provides the current crew roster of the ISS.
	
	3. 'pass [latitude] [longitude]' - provides the time and duration of
	flyover by the ISS for the given [latitude] and [longitude] user input
	variables. [latitude] is constrained to be between -90 and 90 degrees
	whereas [longitude] is constrained to be between -180 and 180 degrees.
	
	The collection and formatting of these informations is handled by the
	question class whose details can be found in question.py in the
	same subdirectory as this file."""

# If there were no command line arguments, error out

	if len(sys.argv) < 2:

		print("Error: Command line option must follow program invocation. Please provide one of the following keywords as a command line argument to this program: 'loc', 'pass', or 'people'. Please see the user manual for further information.\n")

		return

# Take in the command line arguments

	opt = sys.argv[1] 

	if len(sys.argv) > 2:

		args = [arg for arg in sys.argv[2:]]

	else:

		args = []

# Let the user know they have successfully entered the program

	print("\nWelcome to the ISS status check engine!\n")

# Initiate an instance of the question class
## The instance of the question class
	query = question()

# Have the question class check the input for correctness  

	query.check_input(opt, args)

# If the input is bad query.exit will be set to 1, exit as such
# No need for an error message, query will have already handled that

	if query.exit > 0:

		return

# Have the question class respond to the request posed by the input

	query.respond()

# Let the user know they have exited the program successfully

	print("Thank you for using the ISS status check engine!\n")

if __name__ == "__main__":

	main()

