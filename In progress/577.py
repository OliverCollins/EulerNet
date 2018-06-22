# Programmer:    Oliver Collins
# Date:          May 14th, 2018
# Language:      Python

'''
-- -- -- -- -- -- -- -- -- -- --
'''

# Counting hexagons
# Not Solved

def construct_triangle(n):
	triangle_cords = []
	for y in range(n+1):
		for x in range(y, n+1):
			if y % 2 == 0:
				triangle_cords.append([x - (y * 0.5), y])
			else:
				triangle_cords.append([x - (y * 0.5), y])
	return triangle_cords

triangle = construct_triangle(3)

for x in range(len(triangle)):
	start = triangle[x]
	for y in range(6):
		if [triangle[x][0] - 0.5, triangle[x][1] + 1] in triangle:
			 pass
