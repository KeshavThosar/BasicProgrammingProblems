'''
Create a program that asks the user to enter their name and their age. 
Print out a message addressed to them that tells them the year that 
they will turn 100 years old.
'''

import datetime
now = datetime.datetime.now()
current_year = now.year
name = input("Please enter your name: ")
age = int(input("Please enter your age:  "))
hundred_year = current_year - age + 100
print("Hello ", name.capitalize(), ",you are going to turn hundred in the year: ", hundred_year)