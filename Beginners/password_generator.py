'''
Write a password generator in Python.
Be creative with how you generate passwords:
	strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. 
The passwords should be random, generating a new password every time the user asks for a new password. 
Include your run-time code in a main method.
'''
from random import randint
password_length = 12
password_chars = 'qwertyuiop[]#asdfghjkl;zxcvbnm,./!"@$%^&*()_-<>?'
password_char_index = [randint(0, len(password_chars)-1) for i in range(password_length)]
password = [password_chars[i] for i in password_char_index]
for i in range(0,randint(0,len(password)-1)):
	random_index = randint(0,len(password)-1)
	password[random_index] = password[random_index].upper()
password = ''.join(password) 
print('Password: ', password)