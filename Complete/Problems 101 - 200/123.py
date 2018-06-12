# Programmer:    Oliver Collins
# Date:          June 11th, 2018
# Language:      Python

'''
----------------------------------
'''

# Prime square remainders
# Solved

import math

n, nums = 1000000, {}

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

primes = list(d.keys())

n = 1

while True:
	current_prime = primes[n]

	# Check to see if the value for n for which the remainder exceeds 10^10
	if ((current_prime-1)**n + (current_prime+1)**n) % current_prime**2 > 1e9:
		print(n)
		break
	else:
		n += 1
