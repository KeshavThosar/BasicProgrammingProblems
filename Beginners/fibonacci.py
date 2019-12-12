x1 = 0
x2 = 1
fib = [x1, x2]
limit = int(input('Enter a limit: '))
for i in range(0, limit - 2):
	x3 = x1 + x2
	fib.append(x3)
	x1 = x2
	x2 = x3
print(*fib)