import random

def Main():
	answer = str(random.randint(1000,9999))
	prediction = input('Enter a 4 digit number:  ')
	cows = 0
	bulls = 0
	i=0
	for char in prediction:
		if char in answer:
			if prediction[i] == answer[i]:
				cows += 1
			else:
				bulls += 1
		i += 1
	print('Actual answer: ',answer)
	print('Your prediction: ', prediction)
	print('Cows: ', cows, ' Bulls: ', bulls)

if __name__ == '__main__':
	Main()