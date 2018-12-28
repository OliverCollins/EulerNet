# Programmer:    Oliver Collins
# Date:          December 27th, 2018
# Language:      Python

'''
----------------------------------
'''

# Powerful digit sum
# Solved

max_count = 0

for a in range(2, 100):
	for b in range(2, 100):
		if sum(int(digit) for digit in str(a**b)) > max_count:
			max_count = sum(int(digit) for digit in str(a**b))
print(max_count)
