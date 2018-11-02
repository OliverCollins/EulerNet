import math

def sum_digits3(n):
	r = 0
	while n:
		r, n = r + n % 10, n // 10
	return r

def isInt(n):
	if n % 2 == 0 or (n+1) % 2 == 0:
		return True
	return False

a, current_num = [], 11

while len(a) < 9:

	sum_digits = sum_digits3(current_num)

	if sum_digits != 1:
		if isInt(math.log(current_num, sum_digits)):
			a.append(current_num)

	current_num += 1

print(a)