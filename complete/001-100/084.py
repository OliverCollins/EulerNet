# Programmer:    Oliver Collins
# Date:          December 27th, 2018
# Language:      Python

'''
----------------------------------
'''

# Monopoly odds
# Solved

import random
from random import shuffle

spaces, game_length, current_space = range(40), 100000, 0
num_doubles, ending_space = 0, []

# Cards
community_chess = ['GO', 'JAIL']
chance = ['GO', 'JAIL', 'C1', 'E3', 'H2', 'R1', 'next_railroad', 'next_railroad', 'next_utility', 'back_3']

for turn in range(0, game_length):

	# Roll the dice
	dice1 = random.randint(1,4)
	dice2 = random.randint(1,4)

	# Check to see if doubles
	if dice1 == dice2:

		num_doubles += 1

		# Go to jail for rolling 3 consecutive doubles
		if num_doubles == 3:
			current_space = 10
			num_doubles = 0
			ending_space.append(current_space)
			continue

	else:
		num_doubles = 0

	current_space += (dice1 + dice2)

	# Pass GO
	if current_space >= 40:
		current_space = current_space - 40

	# Community Chest (1 in 8 chance to move)
	if random.randint(1,16) < 3:
		if current_space == 2 or current_space == 17 or current_space == 33:
			# Draw card from community chess pile
			card = community_chess[0]
			if card == 'GO':
				current_space = 0
			if card == 'JAIL':
				current_space = 10

		# Put card on the bottom
		community_chess[:] = community_chess[1:] + community_chess[:1]

	# Chance (5 in 8 chance to move)
	if random.randint(1,8) < 6:
		if current_space == 7 or current_space == 22 or current_space == 36:
			card = chance[0]
			if card == 'GO':
				current_space = 0
			if card == 'JAIL':
				current_space = 10
			if card == 'C1':
				current_space = 11
			if card == 'E3':
				current_space = 24
			if card == 'H2':
				current_space = 39
			if card == 'R1':
				current_space = 5
			if card == 'next_railroad':
				if current_space == 7:
					current_space = 15
				if current_space == 22:
					current_space = 25
				if current_space == 36:
					current_space = 5
			if card == 'next_utility':
				if current_space == 7 or current_space == 36:
					current_space = 12
				if current_space == 22:
					current_space = 28
			if card == 'back_3':
				current_space = current_space - 3

			# Put card on the bottom
			chance[:] = chance[1:] + [chance[0]]

	# Go To Jail
	if current_space == 30:
		current_space = 10

	ending_space.append(current_space)

top_matches = 3
for x in range(0, top_matches):
	highest = max(set(ending_space), key=ending_space.count)
	ending_space[:] = [x for x in ending_space if x != highest]
	print(highest, end='')
print()