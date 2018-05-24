# Programmer:    Oliver Collins
# Date:          May 20th, 2018
# Language:      Python

'''
----------------------------------
'''

# Largest Palidrome Product
# Solved

num1, num2, current_largest = 100, 100, 0

# Keep looping until highest two numbers multiplied is reach
while num1 * num2 < 999**2:
	num = str(num1 * num2)
	str1, str2 = num[0:3], num[3:6]
	str2 = str2[::-1]

	# If palindrome
	if int(str1) == int(str2):
		if num1 * num2 > current_largest:
			current_largest = num1 * num2

	# If second number is 999 or greater reset number
	if num2 > 998:
		num2 = 100
		num1 += 1
	else:
		num2 += 1
		
print(current_largest)
