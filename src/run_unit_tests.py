#!/home/dwooten/anaconda3/bin/python

# Creator: Daniel Wooten
# Date: 05/22/2020
# verison 1.0

# This file contains the unit testing infrastructure

from source.iss import iss

def version_test():
	"""Tests to see if the iss class returns its version number correctly"""

	expected_value = 1

# Get an instance of the class to work with

	station = iss()

# Check if the version number is correct

	test_value = station.version

	if test_value == expected_value:

		return(1)

	else:

		return(0)


def main():
	"""Manages the execution of the unit tests"""

	print("\nBegining unit tests.\n")

	tests = {}

# Attempt to open a file to return tests results

	try:	

		out_file = open("Test.test", "w")

	except OSError:

		print("Failed to open Test.test. Exiting gracefully.\n")

		return()

# Give a header to the test file

	out_file.write("********************************************************************************\n")

	out_file.write("********************************************************************************\n\n")

	out_file.write("Unit Testing Report\n\n")

	out_file.write("********************************************************************************\n")

	out_file.write("********************************************************************************\n\n")

# Populate the tests dictionary and in doing so call and execute the tests

	tests['version_test'] = version_test()

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
