def prob(x):
	return (1 - (x/343.195459424716858620))

total_prob = 1
for distance in range(1, 51):
	 total_prob *= prob(distance)

print(total_prob)
