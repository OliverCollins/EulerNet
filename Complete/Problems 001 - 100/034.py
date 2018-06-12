# Programmer:    Oliver Collins
# Date:          June 11th, 2018
# Language:      Python

'''
----------------------------------
'''

# Digit factorials
# Solved


# Get factorial of a number
def factorial(n):
	total = 1
	for x in range(n, 1, -1):
		total *= x
	return total

sum_, curious_nums = 0, []

# Loop through numbers until 1,000,000 since it's impossible to go over
for nums in range(3, 1000000):
	str_num = str(nums)

	# Loop through each digit in number and get factorial
	for digit in range(len(str_num)):
		sum_ += factorial(int(str_num[digit]))

	# Check to see if curious number
	if sum_ == nums:
		curious_nums.append(nums)
	sum_ = 0

print(sum(curious_nums))
