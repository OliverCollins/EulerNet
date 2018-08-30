# Programmer:    Oliver Collins
# Date:          May 14th, 2018
# Language:      Python

'''
-- -- -- -- -- -- -- -- -- -- --
'''

# Counting primitive Pythagorean triples
# Not Solved

import math

N, n_1, n_v, ctr = 100, 0, 0, 0
for i in range(math.ceil(math.sqrt((2*N)/(1 + (1 + math.sqrt(2)))**2))):
	if i % 2 == 1:
		n_1 = math.ceil(i / math.sqrt(2)) + 1
		n_v = math.ceil((math.sqrt(2*N - i**2) - i) / 2)
		for j in range(n_1, n_v):
			if (i or j == 1):
				ctr += 1
	print(i)

for i in range(math.ceil(math.sqrt((N)/(1 + (1 + math.sqrt(2))**2)))):
	n_1 = i * math.ceil(math.sqrt(2)) + 1
	n_v = math.ceil(math.sqrt(N - i**2)) - i
	

'''

import math

n = int(1e3)

def common_data(list1, list2):
	for x in list1:
		for y in list2:
			if x == y:
				return True
	return False

def divisors(num):
	divs = []
	for x in range(2, math.ceil(num / 2) + 1):
		if num % x == 0:
			divs.append(x)
	divs.append(num)
	return divs

for a in range(1, n):
	for b in range(a+1, n):
		for c in range(b+1, n):
			# Pythagorean triplet
			if a**2 + b**2 == c**2:

				# Check to see if co-prime
				if not common_data(divisors(a), divisors(b)) and not common_data(divisors(b), divisors(c)) and not common_data(divisors(a), divisors(c)):
					print(a, b,  c)

'''

# http://vixra.org/pdf/1310.0211v1.pdf
