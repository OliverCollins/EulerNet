# Programmer:    Oliver Collins
# Date:          June 21st, 2018
# Language:      Python

'''
----------------------------------
'''

# Self powers
# Solved

sum_ = 0

for x in range(1, 1001):
	sum_ += x**x

print(str(sum_)[-10:])
