# Programmer:    Oliver Collins
# Date:          June 1st, 2018
# Language:      Python

'''
----------------------------------
'''

# Double-base palindromes
# Solved

def is_palindrome(n):
	rev = ''.join(reversed(n))
	if n == rev:
		return True
	return False

sum_ = 0

for x in range(1000000):
	if is_palindrome(str(x)):
		if is_palindrome(str(bin(x)[2:])):
			sum_ += x

print(sum_)
