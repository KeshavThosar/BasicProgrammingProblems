'''
Ask the user for a number and determine whether the number is prime or not. 
'''
number = int(input('Enter a number: '))
factors = [x for x in range(1, number+1) if number%x == 0]
if number > 1:
	if len(factors) < 3:
		print(number, ' is a prime number')
	else:
		print(number, ' is a composite number with factors: ', factors)
elif number == 1:
	print(number, ' is neither prime nor composite') 