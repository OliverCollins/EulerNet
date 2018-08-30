# Programmer:    Oliver Collins
# Date:          May 14th, 2018
# Language:      Python

'''
-- -- -- -- -- -- -- -- -- -- --
'''

# Non-bouncy numbers
# Not Solved

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

not_bouncy = 100

for x in range(100, 100000000):
	if not is_bouncy(str(x)):
		not_bouncy += 1

print(not_bouncy)
