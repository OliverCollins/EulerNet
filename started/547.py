# Programmer:    Oliver Collins
# Date:          May 14th, 2018
# Language:      Python

'''
-- -- -- -- -- -- -- -- -- -- --
'''

# Distance of random points within hollow square laminae
# Not Solved

import random
import math

a = []
for x in range(1000000):
	p1_x, p1_y = 1 * random.random(), 1 * random.random()
	p2_x, p2_y = 1 * random.random(), 1 * random.random()
	a.append(math.sqrt(((p2_x - p1_x)**2) + ((p2_y - p1_y)**2)))

print(sum(a) / len(a))
