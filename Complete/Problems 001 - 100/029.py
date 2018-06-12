# Programmer:    Oliver Collins
# Date:          June 11th, 2018
# Language:      Python

'''
----------------------------------
'''

# Distinct powers
# Solved

combinations = []

# Loop through values and add to combination list 
for a in range(2, 101):
	for b in range(2, 101):
		combinations.append(a**b)

# Print distinct combinations
print(len(set(combinations)))
