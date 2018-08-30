# Programmer:    Oliver Collins
# Date:          June 1st, 2018
# Language:      Python

'''
----------------------------------
'''

# Integer right triangles
# Solved

import math

solutions, n, num_solutions = 0, 4, [0]

# Loop through p-values
while n <= 1000:

	# Loop through potential a, b, and c values
	for a in range(math.floor(math.sqrt(n)), math.floor(n / 3)):
		for b in range(a + 1, n - (2 * a)):
			for c in range(n - a - b, n - b):

				# Check to see if perimeter adds to n and if values add to a right angle triangle
				if a + b + c == n:
					if a**2 + b**2 == c**2:
						solutions += 1
	num_solutions.append(solutions)

	# n will be even
	n += 4
	solutions = 0

max_value = max(num_solutions)
max_index = num_solutions.index(max_value)
print(max_value, 4 * max_index)
