# Programmer:    Oliver Collins
# Date:          June 11th, 2018
# Language:      Python

'''
----------------------------------
'''

# Coded triangle numbers
# Solved

file = open("words.txt", "r")
f = file.read()

# Split words by comma
f = f.split(',')

# Go through list and remove excess ""
for x in range(len(f)):
	f[x] = f[x].replace("\"", "")

triangle_sum, word_value, triangle_numbers = 0, 0, []

# Get 1000 triangle numbers
for x in range(0, 1000):
	triangle_numbers.append(x * (x + 1) / 2)

# Loop through every word
for word in range(len(f)):

	# Loop through every character
	for char in range(len(f[word])):

		# Get the word value
		word_value += ord(f[word][char]) - 64

	# Check to see if it's a triangle number
	if word_value in triangle_numbers:
		triangle_sum += 1
	word_value = 0

print(triangle_sum)
