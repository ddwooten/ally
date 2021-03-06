#!/home/dwooten/anaconda3/bin/python

## @package run_unit_tests
# This file contains all unit tests and the test running infrastructure.
#
# Test information is output to the created file unit_Tests.test.
#
# Creator: Daniel Wooten
# Date: 05/22/2020
# verison 1.0

from source.question import question 

def bad_option_test():
	"""Tests to see if the question class sets its exit status to 1
	following the input of a bad command line argument"""
	
	##@var expected_value
	# passing value for the test
	expected_value = 1

# Get an instance of the class to work with
	
	##@var query
	# instance of the question class
	query = question()

# Creat fake user input

	##@var opt
	# fake user input option
	opt = "fake"

	##@var args
	# fake user input options
	args = ["-95", "175"]

	query.check_input(opt, args)

# Get the value to check which in this case is the exit status

	test_value = query.exit

# Check the value and report

	if test_value == expected_value:

		return(1)

	else:

		return(0)

def version_test():
	"""Tests to see if the iss class returns its version number correctly"""

	##@var expected_value
	# passing value for the test
	expected_value = 1

# Get an instance of the class to work with

	##@var station
	# instance of the question class
	station = question()

# Check if the version number is correct

	test_value = station.version

	if test_value == expected_value:

		return(1)

	else:

		return(0)

def main():
	"""Manages the execution of the unit tests"""

	print("\nBegining unit tests.\n")

	##@var tests
	# dictionary for holding all unit tests to be executed
	tests = {}

# Attempt to open a file to return tests results

	try:	

		out_file = open("unit_Test.test", "w")

	except OSError:

		print("Failed to open unit_Test.test. Exiting gracefully.\n")

		return()

# Give a header to the test file

	out_file.write("********************************************************************************\n")

	out_file.write("********************************************************************************\n\n")

	out_file.write("Unit Testing Report\n\n")

	out_file.write("********************************************************************************\n")

	out_file.write("********************************************************************************\n\n")

# Populate the tests dictionary and in doing so call and execute the tests

	tests['version_test'] = version_test()

	tests['bad_option_test'] = bad_option_test()

# Initilize some counter varaibles

	total_tests = 0

	pass_tests = 0

	fail_tests = 0

# Loop through the testing dictionary, executing the tests and logging the
# outcomes

	for key in tests.keys():

		total_tests += 1

		if tests[key] > 0:

			pass_tests += 1

			out_file.write("Test {}: PASS\n\n".format(key))

		else:

			fail_tests += 1

			out_file.write("Test {}: FAIL\n\n".format(key))


	out_file.write("********************************************************************************\n")

	out_file.write("********************************************************************************\n\n")

	out_file.write("Unit Testing Report Concluding Details\n\n")

	out_file.write("********************************************************************************\n")

	out_file.write("********************************************************************************\n\n")

	out_file.write("Tests passed / total: {} / {}\n\n".format(pass_tests,
							          total_tests))

	out_file.close()

	print("Unit testing has concluded.\n\n")

if __name__ == '__main__':
	
	main()
