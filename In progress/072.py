# Programmer:    Oliver Collins
# Date:          July 3rd, 2018
# Language:      Python

'''
-- -- -- -- -- -- -- -- -- -- --
'''

# Counting fractions
# Not Solved

import math

count, end_value = 0, 1000

for d in range(2, end_value):
	for n in range(2, d):

		# Check to see if fraction is completely reduced
		if math.gcd(n, d) == 1:
			count += 1

print(count + end_value - 2)
