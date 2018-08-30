# Programmer:    Oliver Collins
# Date:          May 14th, 2018
# Language:      Python

'''
-- -- -- -- -- -- -- -- -- -- --
'''

# Pentagon numbers
# Not Solved

pentagonal_nums, n = [], 1

while True:
	pentagonal_nums.append(int(n * (3 * n - 1) / 2))
	n += 1

	if (n == 11):
		break

print(pentagonal_nums)
