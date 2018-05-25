# Programmer:    Oliver Collins
# Date:          May 18th, 2018
# Language:      Python

'''
----------------------------------
'''

# Highly Divisible Triangular Numbers
# Solved

import math

# Loop through number and get divisors
def divisors(num):
	divs = []
	for x in range(1, math.ceil(num / 2) + 1):
		if num % x == 0:
			divs.append(x)
	divs.append(num)
	return divs

triangle, current_num = [0], 0

# Loop until you get a triangle number with 500 divisors
while len(divisors(current_num)) < 500:

	# Get the next triangle number
	triangle.append(triangle[len(triangle) - 1] + 1)
	current_num += triangle[len(triangle) - 1]

	# Loop through numbers that have a higher probability of having more divisors
	while (current_num % 4 != 0 or current_num % 60 != 0 or current_num % 100 != 0):
		triangle.append(triangle[len(triangle) - 1] + 1)
		current_num += triangle[len(triangle) - 1]

print(current_num)
