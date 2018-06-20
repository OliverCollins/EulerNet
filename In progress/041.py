# Programmer:    Oliver Collins
# Date:          May 14th, 2018
# Language:      Python

'''
-- -- -- -- -- -- -- -- -- -- --
'''

# Pandigital prime
# Not Solved

from itertools import permutations
import math

def is_prime(n):
	for x in range(2, round(math.sqrt(n))):
		if n % x == 0:
			return False
	return True

nums = [''.join(p) for p in permutations('987654320')]

for x in range(len(nums)):
	if int(nums[x]) % 2 != 0:
		if is_prime(int(nums[x])):
			print(nums[x])
			break
