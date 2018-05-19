# Programmer:    Oliver Collins
# Date:          May 18th, 2018
# Language:      Python

'''
----------------------------------
'''

# Largeest Collatz sequence
# Solved

num, current_val, longest_chain, current_chain, num_with_longest_chain = 1, 1, [], [], 0

# Loop through all numbers until 100,000
while (num < 1000000):

	# While value hasn't reached 1 follow Collatz rules
	while (current_val != 1):
		if current_val % 2 == 0:
			current_val /= 2
		else:
			current_val = (3 * current_val) + 1

		# Append the value to the current chain
		current_chain.append(current_val)

		# Check to see length of the current chain is the largest
		if (len(current_chain) > len(longest_chain)):
			longest_chain = current_chain
			num_with_longest_chain = num
	num += 1
	current_val = num
	current_chain = []

print(num_with_longest_chain, len(longest_chain))
