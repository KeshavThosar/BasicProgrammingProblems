'''
Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order. For example, say I type the string:
	My name is Michele
Then I would see the string:
  Michele is name My
shown back to me.
'''
def reverse_word_order(string):
	words = string.split(' ')
	return ' '.join(words[::-1])
print('My name is Michele')
print(reverse_word_order('My name is Michele'))