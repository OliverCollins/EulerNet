# Programmer:    Oliver Collins
# Date:          May 15th, 2018
# Language:      Python

'''
----------------------------------
'''

# Large Prime Numbers
# Solved

def get_next_prime(n):
	num, prime = n + 2, False
	while not prime:
		for x in range(2, num):
			if (num % x == 0):
				break
			if (x == num - 1):
				prime = True
		num += 1
	return num - 1

prime_numbers = [2, 3]
while len(prime_numbers) < 10001:
	prime_numbers.append(get_next_prime(prime_numbers[len(prime_numbers) - 1]))
print(prime_numbers[len(prime_numbers) - 1])
