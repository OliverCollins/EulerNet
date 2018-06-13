# Programmer:    Oliver Collins
# Date:          June 12th, 2018
# Language:      Python

'''
----------------------------------
'''

# Prime permutations
# Solved

import math

n, nums = 10000, {}

# Fill dictionary with numbers
for x in range(2, n+1):
	nums[x] = True

# Sieve of Eratosthenes
for x in range(2, math.ceil(math.sqrt(n))):
	if nums[x] is True:
		for y in range(x**2, n+1, x):
			nums[y] = False

# Grab only prime numbers from dictionary
primes = list(dict((k, v) for k, v in nums.items() if v == True).keys())
index = 0

# Find index of first prime number above 1,000
for x in range(len(primes)):
	if primes[x] > 1000:
		index = x
		break

# Just get prime numbers between 1,000 and 10,000
new_primes = primes[index:]

for a in range(len(new_primes)):
	for b in range(a, len(new_primes)):
		for c in range(b, len(new_primes)):

			# If each term increases by same number
			if ((new_primes[c] - new_primes[b]) == (new_primes[b] - new_primes[a])):
				
				# Check to make sure they aren't the same number
				if (new_primes[c] != new_primes[b]):

					# If the three numbers are permutations of each other
					if (sorted(str(new_primes[c])) == sorted(str(new_primes[b]))) and (sorted(str(new_primes[b])) == sorted(str(new_primes[a]))):
						print(new_primes[a], new_primes[b], new_primes[c])

			# Since difference from a, b, and c can't be more than 4500 apart
			if (new_primes[b] - new_primes[a]) > 4500:
				break
