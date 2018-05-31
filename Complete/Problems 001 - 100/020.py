# Programmer:    Oliver Collins
# Date:          May 30th, 2018
# Language:      Python

'''
----------------------------------
'''

# Factorial digit sum
# Solved

fact, sum_ = 1, 0

# Get factorial for 100
for x in range(1, 101):
	fact *= x

# Add all digits together
for x in range(len(str(fact))):
	sum_ += int(str(fact)[x])

print(sum_)
