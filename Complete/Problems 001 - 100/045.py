# Programmer:    Oliver Collins
# Date:          May 26th, 2018
# Language:      Python

'''
----------------------------------
'''

# Triangular, pentagonal, and hexagonal
# Solved

import math

triangle = pentagonal = hexagonal = 1

# Start at where the last verified triangle, pentagonal, and hexagonal values were found
# Check for now until 100000 and increase if we can't find values there
for tri in range(286, 100000):

	# Pentagonal values are roughly 3 times the value of triangular values
	for pent in range(math.floor(tri / math.sqrt(3)) - 3, math.floor(tri / math.sqrt(3)) + 3):

		# Hexagonal values are roughly 4 times the value of triangular values
		for hexa in range(math.floor(tri / 2) - 3, math.ceil(tri / 2) + 3):

			# Calculate the values for triangle, pentagonal, and hexagonal values
			triangle = tri * (tri + 1) / 2
			pentagonal = pent * (3 * pent - 1) / 2
			hexagonal = hexa * (2 * hexa - 1)

			# Check to see if they are equal to each other, and if so, print and exit
			if triangle == pentagonal:
				if triangle == hexagonal:
					print(triangle)
					exit()
