#!/home/dwooten/anaconda3/bin/python

# Author: Daniel Wooten
# Date: 05/22/2020
# Version: 1.0

# This is the executing program for the data challenge - this function is what
# you run in the command line

import sys 

from question import question


def main():
	"""Iss information retreival program. """

# Take in the command line arguments

	opt = sys.argv[1:] 

	if len(sys.argv) > 2:

		args = [arg for arg in sys.argv[2:]]

	else:

		args = []

# Let the user know they have sucessfully entered the program

	print("Welcome to the ISS status check engine!\n")

# Initiate an instance of the question class

	query = question()

# Have the question class check the input for correctness  

	query.check_input(opt, args)

# Have the question class respond to the reqest posed by the input

	query.respond()

# Let the user know they have exited the program sucessfully

	print("Thank you for using the ISS status check engine!\n")

if __name__ == "__main__":

	main()

