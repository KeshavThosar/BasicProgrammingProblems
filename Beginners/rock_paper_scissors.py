from random import randint
choices = ['Rock', 'Paper', 'Scissors']
print('Welcome to Rock, Paper, Scissors')
outcomes = ["It's Tie", 'You Win!', 'Better Luck next time']
while True:
	print('1) Rock', '2) Paper', '3) Scissors', end='\n')#
	rand_choice = randint(1,3)
	user_choice = int(input('Please enter a choice: '))
	print("Computer's choice: ", choices[rand_choice-1])
	print('Your choice: ', choices[user_choice-1])
	if user_choice == rand_choice:
			print(outcomes[0])
	elif (user_choice == 1 and rand_choice == 2) or (user_choice == 2 and rand_choice == 3) or (user_choice == 3 and rand_choice == 1):
			print(outcomes[2])
	else:
		print(outcomes[1])
		break
	print('')