# Programmer:    Oliver Collins
# Date:          May 17th, 2018
# Language:      Python

'''
----------------------------------
'''

# Pythagorean triplet
# Solved

for a in range(1, 999):
	for b in range(a+1, 999):
		for c in range(b+1, 999):

			if (a + b + c > 1000):
				break

			# Pythagorean triplet
			if ((a**2) + (b**2) == (c**2)):
				if a + b + c == 1000:
					print(a * b * c)
					exit()
