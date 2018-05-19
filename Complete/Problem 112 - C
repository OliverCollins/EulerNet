# Programmer:    Oliver Collins
# Date:          May 18th, 2018
# Language:      Python

'''
----------------------------------
'''

# Bouncy numbers
# Solved

def is_bouncy(n):

	# Decreasing
	if int(n[0]) > int(n[1]):
		for x in range(1, len(n) - 1):
			if int(n[x]) < int(n[x + 1]):
				return True

	# Increasing
	elif int(n[0]) < int(n[1]):
		for x in range(1, len(n) - 1):
			if int(n[x]) > int(n[x + 1]):
				return True

	# If first two numbers are the same
	else:

		# Keep looking until one number is either higher or lower
		for x in range(0, len(n) - 1):
			if int(n[x]) == int(n[x+1]):
				continue

			# Decreasing
			elif int(n[x]) > int(n[x+1]):
				for x in range(1, len(n) - 1):
					if int(n[x]) < int(n[x + 1]):
						return True
				break

			# Increasing
			elif int(n[x]) < int(n[x+1]):
				for x in range(1, len(n) - 1):
					if int(n[x]) > int(n[x + 1]):
						return True
				break

	return False

bouncy, not_bouncy, num = 0, 99, 200

for x in range(100, 200):
	if is_bouncy(str(x)):
		bouncy += 1
	else:
		not_bouncy += 1

while bouncy / (bouncy + not_bouncy) != 0.99:
	if is_bouncy(str(num)):
		bouncy += 1
	else:
		not_bouncy += 1
	num += 1

print(num - 1)
