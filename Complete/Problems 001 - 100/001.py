# Programmer:    Oliver Collins
# Date:          May 15th, 2018
# Language:      Python

'''
----------------------------------
'''

# Multiples of 3 and 5
# Solved

n, sum_ = 3, 0
while n != 1000:
	if (n % 3 == 0 or n % 5 == 0):
		sum_ += n
	n += 1
print(sum_)
