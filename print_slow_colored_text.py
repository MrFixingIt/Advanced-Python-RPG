import sys
import time

my_string = "Hello World! Hello World! Hello World! Hello World! Hello World! Hello World! Hello World! Hello World! Hello World! Hello World!"
"Hello World! Hello World! Hello World! Hello World! Hello World! Hello World! Hello World! Hello World! Hello World! Hello World!"

def slow_print(string_to_print):
	for letter in string_to_print:
		sys.stdout.write(letter)
		sys.stdout.flush()
		time.sleep(0.035)
	print("")

slow_print(my_string)

# ---------------------------------------------------------------------------------------------------------------------
# 6:38
# For colored text see...
# Week4 Nested Data Structures (Code Demo Bonus)

