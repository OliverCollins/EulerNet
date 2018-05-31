# Programmer:    Oliver Collins
# Date:          May 30th, 2018
# Language:      Python

'''
----------------------------------
'''

# Amicable numbers
# Solved

import math

def divisors(num):
	divs = []
	for x in range(1, math.ceil(num / 2) + 1):
		if num % x == 0:
			divs.append(x)
	divs.append(num)

	# Return divisors without n included
	return divs[:-1]

divs, amicable_sum = [], 0

for nums in range(1, 10000):
	divs.append(divisors(nums))

for x in range(len(divs)):
	a, b = x+1, sum(divisors(sum(divs[x])))

	# Check to see if div(a) == b
	if a == b:

		# Check to see if a != b
		if a != sum(divs[x]):
			amicable_sum += x+1

print(amicable_sum)
