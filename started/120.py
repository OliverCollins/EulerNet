r_max, list_r = 0, []

# Loop through all a and n values
for a in range(3, 1001):

	# Found that r_max will be in range from 1/3a -> a-1
	for n in range(round(a/3.33334), a):

		if (((a-1)**n) + ((a+1)**n)) % a**2 > r_max:
			r_max = (((a-1)**n) + ((a+1)**n)) % a**2

	# Don't need to reset r_max since it will always be higher
	list_r.append(r_max)

# Get the sum of list
print(sum(list_r))