# Programmer:    Oliver Collins
# Date:          May 21st, 2018
# Language:      Python

'''
----------------------------------
'''

# Large Prime Numbers
# Solved

import math

n, nums = 2000000, {}

# Fill dictionary with numbers
for x in range(2, n+1):
	nums[x] = True

# Sieve of Eratosthenes
for x in range(2, math.ceil(math.sqrt(n))):
	if nums[x] is True:
		for y in range(x**2, n+1, x):
			nums[y] = False

# Grab only prime numbers from dictionary
d = dict((k, v) for k, v in nums.items() if v == True)
print(sum(d.keys()))
