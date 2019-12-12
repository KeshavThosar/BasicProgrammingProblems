'''
Write a program that takes a list of numbers 
(for example, a = [5, 10, 15, 20, 25]) 
and makes a new list of only the first and last elements of the given list.
For practice, write this code inside a function.
'''
def first_and_last(input_list):
	return [input_list[0], input_list[-1]]


a = [5, 10, 15, 20, 25]
print('a: ', a)
print(first_and_last(a))