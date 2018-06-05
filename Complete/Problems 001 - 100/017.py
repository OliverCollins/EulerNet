# Programmer:    Oliver Collins
# Date:          June 4th, 2018
# Language:      Python

'''
-- -- -- -- -- -- -- -- -- -- --
'''

# Number letter counts
# Solved

letter_count = 0

# Count all the times the word 'hundred' is used
letter_count += len('hundred') * 900

# Count all the times these numbers come before 'hundred', or  after 'twenty', etc. Exclude when between 10-19
letter_count += len('one') * 190
letter_count += len('two') * 190
letter_count += len('three') * 190
letter_count += len('four') * 190
letter_count += len('five') * 190
letter_count += len('six') * 190
letter_count += len('seven') * 190
letter_count += len('eight') * 190
letter_count += len('nine') * 190

# Count each occurence in each 'hundred'
letter_count += len('ten') * 10
letter_count += len('eleven') * 10
letter_count += len('twelve') * 10
letter_count += len('thirteen') * 10
letter_count += len('fourteen') * 10
letter_count += len('fifteen') * 10
letter_count += len('sixteen') * 10
letter_count += len('seventeen') * 10
letter_count += len('eighteen') * 10
letter_count += len('nineteen') * 10

# Count the tens
letter_count += len('twenty') * 100
letter_count += len('thirty') * 100
letter_count += len('forty') * 100
letter_count += len('fifty') * 100
letter_count += len('sixty') * 100
letter_count += len('seventy') * 100
letter_count += len('eighty') * 100
letter_count += len('ninety') * 100

# Count 'and's (exclude every hundred spot)
letter_count += len('and') * 99 * 9

# Count one-thousand
letter_count += len('onethousand')

print(letter_count)
