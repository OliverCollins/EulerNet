# Programmer:    Oliver Collins
# Date:          June 16th, 2018
# Language:      Python

'''
----------------------------------
'''

# Champernowne's constant
# Solved

string, value, upper = ".", 1, 7

# Make Champernowne's constant
for x in range(1, 10**upper):
	string += str(x)

# Get value of digits multiplied together
for y in range(0, upper):
	value *= int(string[(10**y)])

print(value)
