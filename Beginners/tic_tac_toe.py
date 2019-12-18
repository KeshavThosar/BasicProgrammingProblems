import numpy as np
import subprocess as sp

board_size = 3
'''
r1 = ' --- '*board_size
r2 = ' |'+choice+'| '*board_size
print(r1)
for i in range(0,board_size):
	print(r2)
	print(r1)
'''
board = np.zeros((board_size,board_size))
def multimap(input_list,function_array):
	for function in function_array:
		input_list = map(function, input_list)
	return list(input_list)
def check_game_status():
	status = ('Please continue','P1 wins!', 'P2 wins!', "It's a Tie")
	checks = []
	status_code = 0
	#row check
	for row in board:
		checks.append(row)
	#column check (because, transpose will change the column to row and vice versa)
	for row in board.T:
		checks.append(row)
	checks.append(np.diagonal(board)) #diagonal
	checks.append(np.diag(np.rot90(board))) #opposite diagonal
	checks = multimap(checks, [set,list])
	identical_rows = [x for x in checks if len(x) == 1]
	if 0.0 in board:
		status_code = 0
		if [1.0] in identical_rows:
			status_code = 1
		elif [2.0] in identical_rows:
			status_code = 2
	else:
		status_code = 3
	
	print(status[status_code])
	return status_code

def ask_input():
	pos = input('Please enter a position in the format (x,y): ')
	tok = [ch for ch in pos]
	position = [r for r in tok if r not in ['(',')',',', ' ']]
	position = tuple(map(int, position))
	return position
def update_board(position, value):
	x = position[0]
	y = position[1]
	if x < board_size and y < board_size:
		if board[x,y] == 0:
			board[x,y] = value
			return 1
		else:
			print('Position already occupied')
	else:
		print('Position on available on the board')
def clear_screen():
	tmp = sp.call('cls',shell=True)
def populate_board():
	for row in board:
		'''
		formatted_row = list(map(int,list(row)))
		formatted_row = list(map(str, formatted_row))'''
		formatted_row = multimap(list(row), [int, str])
		formatted_row = '|'+'|'.join(formatted_row)+'|'
		print('-'*len(formatted_row))
		print(formatted_row)

status_code = check_game_status()
while status_code == 0:
	clear_screen()
	populate_board()
	players = ['P1', 'P2']
	for i in [1,2]:
		print(players[i-1])
		while update_board(ask_input(), i) != 1:
			continue

	status_code = check_game_status()




