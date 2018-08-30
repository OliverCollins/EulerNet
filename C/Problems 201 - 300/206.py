# Programmer:    Oliver Collins
# Date:          May 18th, 2018
# Language:      Python

'''
----------------------------------
'''

# Concealed Square
# Solved

import math

# Start from the smallest number that could be correct
num = math.floor(math.sqrt(1020304050607080900))

# Keep looping until you find an answer
while True:
	n = str(num**2)
	if (n[2] == '2' and n[4] == '3' and n[6] == '4' and n[8] == '5' and n[10] == '6' and n[12] == '7' and n[14] == '8' and n[16] == '9' and n[18] == '0'):
		print(num)
		exit()

	# Speed up process by only iterating through numbers that have a third digit of 2
	if int(n[2]) > 2:
		num += math.floor(math.sqrt(900000000000000))

	# Only squares of 10 have the last digit being 0
	num += 10
