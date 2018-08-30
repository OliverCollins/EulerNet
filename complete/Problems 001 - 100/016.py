# Programmer:    Oliver Collins
# Date:          May 10th, 2018
# Language:      Python

'''
-- -- -- -- -- -- -- -- -- -- --
'''

# Power digit sum
# Solved

sum_, num = 0, list(str(2**1000))
for x in range(len(num)):
	sum_ += int(num[x])
print(sum_)
