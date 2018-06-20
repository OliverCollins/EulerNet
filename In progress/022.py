# Programmer:    Oliver Collins
# Date:          May 14th, 2018
# Language:      Python

'''
-- -- -- -- -- -- -- -- -- -- --
'''

# Names scores
# Not Solved

# Open the file and get contents
file = open("names.txt", "r") 
not_converted = file.readline()
list_words, current_word = [], ""

# Loop through text file and add all names to a list
for x in range(len(not_converted)):

	# Seperate words by comma
	if not_converted[x] == ',':
		list_words.append(current_word)
		current_word = ""
	else:

		# Remove parentheses from words
		if not_converted[x] != "\"":
			current_word += not_converted[x]

# Variables for current score of word and total value
score, total = 0, 0

# Sort the list in alphabetical order
sorted_list = sorted(list_words)

# Loop through our list and get score for each name
for x in range(len(sorted_list)):

	# Loop through each character in word to calculate score
	for y in range(0, len(sorted_list[x])):
		score += ord(sorted_list[x][y]) - 64
	total += (x + 2) * score
	#print(sorted_list[x], score, x + 2, total)
	score = 0

print(total)
