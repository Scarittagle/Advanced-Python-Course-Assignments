#Homework 1
#Collatz Assignment
#WEIWEI SU
#U17420699
#Last Modifed Date: 8/23/2017

def collatz(number):
	if number % 2 == 0:
		return number // 2
	elif number % 2 == 1:
		return 3 * number + 1

def collatz_sequence():
	print('Enter Number:')
	try:
		number = int(input())
	except ValueError:
		print('Invalid input: must be an int')
		return False
	print('OUTPUT:')
	while number != 1:
		number = collatz(number)
		print(number)
	return True

