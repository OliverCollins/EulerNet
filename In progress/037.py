# Programmer:    Oliver Collins
# Date:          May 14th, 2018
# Language:      Python

'''
-- -- -- -- -- -- -- -- -- -- --
'''

# Truncatable primes
# Not Solved

import math

n, nums, num_truncatable, current_num = 10000, {}, 0, 0

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
del d[2], d[3], d[5], d[7]

list_primes = list(d.keys())

# Loop until you have 11 truncatable numbers
while num_truncatable < 3:

	# Loop through current number's digits
	for x in range(0, len(str(list_primes[current_num]))):

		if x == 0:

			# Keep a temp variable so you can remove digits
			temp = list_primes[x]

		else:
			
			# If current substring is prime keep iterating
			if temp in d.keys():
				print(temp)
				temp = int(temp / 10)

			# Else go to the next number
			else:
				current_num += 1
				break

			# If you are at the last digit and it's prime add it to list of truncatable numbers
			if x == len(str(list_primes[current_num])) - 1:
				print(list_primes[x])
				num_truncatable += 1
				break
