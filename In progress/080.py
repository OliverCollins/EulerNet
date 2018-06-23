# Programmer:    Oliver Collins
# Date:          May 14th, 2018
# Language:      Python

'''
-- -- -- -- -- -- -- -- -- -- --
'''

# Square root digital expansion
# Not Solved

from decimal import *

# Get 103 decimal spots
getcontext().prec = 103

squares, num, total = [], "", 0

# Get non-irrational squares
for x in range(2, 11):
	squares.append(x**2)

# Compute sum of first one hundred irrational square roots
for x in range(2, 101):
	if x not in squares:
		num = str(Decimal(x).sqrt())
		for digit in range(100):
			total += int(num[digit+2])

print(total)
