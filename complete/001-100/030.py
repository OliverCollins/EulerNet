# Programmer:    Oliver Collins
# Date:          June 7th, 2018
# Language:      Python

'''
----------------------------------
'''

# Digit fifth powers
# Solved

sum_, list_nums = 0, []

# Loop through possible numbers
for num in range(1000, 1000000):
	str_num = str(num)

	# Loop through each individual digit in number and get 5th power
	for digit in range(len(str_num)):
		sum_ += int(str_num[digit])**5

	# Check to see if sum of fifth powers are equal to number
	if sum_ == num:
		list_nums.append(sum_)
	sum_ = 0

print(sum(list_nums))
