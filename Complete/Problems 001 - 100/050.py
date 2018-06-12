# Programmer:    Oliver Collins
# Date:          June 11th, 2018
# Language:      Python

'''
----------------------------------
'''

# Consecutive prime sum
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

primes, consecutive_primes, sum_, largest_consecutive_primes = list(d.keys()), 0, [], []

# Loop through first five prime numbers
for x in range(5):
	sum_ = []
	sum_.append(primes[x])

	# Loop through primes numbers until sum of consecutive numbers is > n
	for y in range(x+1, len(primes) / 2):
		sum_.append(primes[y])

		# If sum of consecutive primes is prime
		if sum(sum_) in primes:

			# If number of consecutive primes if higher than previous
			if len(sum_) > consecutive_primes:
				consecutive_primes = len(sum_)
				largest_consecutive_primes.append(sum(sum_))

		# Break statement so we don't check primes above n
		if sum(sum_) > n:
			break

# Print the prime number with most consecutive primes added together
print(largest_consecutive_primes[len(largest_consecutive_primes)-1])
