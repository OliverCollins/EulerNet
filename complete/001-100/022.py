

def get_name_value(name):
	val = 0
	for c in name:
		val += (ord(c) - 64)
	return val

file = open("names.txt", "r")

names, current_name = [], ''

# Put all names in file into list
for c in file.read():
	if c == ',':
		names.append(current_name)
		current_name = ''
	elif c != '\"':
		current_name += c

# Forgets to append ALONSO
names.append("ALONSO")

names = sorted(names)
name_score = 0
for counter, value in enumerate(names):
	name_score += ((counter+1) * get_name_value(value))

print(name_score)
