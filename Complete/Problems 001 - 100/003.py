# Programmer:    Oliver Collins
# Date:          April 1st, 2016
# Language:      Python

'''
----------------------------------
'''

# Largest prime factor
# Solved

def prime(n):
	x, boo = 2,  False
	if (n == 2):
		boo = True
		return boo
	while (n % x != 0):
		x += 1
		if ((n - 1) == x):
			boo = True
	return boo
	
def main():
	p = 2
	n = input("Enter a number: ")
	while (n > p):
		if (prime(p)):
			if (n % p == 0):
				n = n / p
				print p
			p += 1
		p += 1
	print n
	
main()
