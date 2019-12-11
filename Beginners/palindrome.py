'''
Ask the user for a string and print out whether this string is a palindrome or not.
'''

string = input('Please enter a string: ')
if string == string[::-1]:
	print(string, ' is a palindrome')
else:
	print(string, ' is not a palindrome')