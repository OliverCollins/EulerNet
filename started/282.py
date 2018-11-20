def A(m, n):
	if m == 0:
		return n+1
	elif (m > 0 and n == 0):
		return A(m-1, 1)
	else:
		return A(m-1, A(m, n-1))

sum_ = 0
for n in range(0, 5):
	sum_ += A(n, n)
	print(sum_)
