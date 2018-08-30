# Programmer:    Oliver Collins
# Date:          May 14th, 2018
# Language:      Python

'''
-- -- -- -- -- -- -- -- -- -- --
'''

# Non-abundant sums
# Not Solved

import math

def divisors(n):
	divs = []
	if n == 1:
		return [1]
	elif n == 2:
		return [1, 2]
	for x in range(1, math.ceil(n / 2)):
		if n % x == 0:
			divs.append(x)
	return divs

abundant_nums = []

for x in range(1, 28123):
	divs = divisors(x)
	if divs != None:
		if sum(divs) > x:
			abundant_nums.append(x)

print(abundant_nums)
