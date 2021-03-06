# Programmer:    Oliver Collins
# Date:          May 14th, 2018
# Language:      Python

'''
-- -- -- -- -- -- -- -- -- -- --
'''

# How many reversible numbers are there below one-billion?
# Solved

def check_odd_digits(num):
	str_num = str(num)
	for x in range(len(str_num)):
		if int(str_num[x]) % 2 == 1:
			return 0
	return 1

sum_ = 0
for x in range(10, 10000000):
	temp = (x + int(str(x)[::-1]))
	if temp % 2 == 0:
		sum_ += check_odd_digits(temp)
print(sum_)
