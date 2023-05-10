#Write a program that asks the user to enter two numbers and compares them using the following comparison operators: `>`, `<`, `>=`, `<=`, `==`, and `!=`. The program should print out the result of each comparison.

#Get the 2 numbers from the user
print('Please kindly provide 2 numbers let\'s compare them')
first_number = int(input('Enter the 1st number:'))
second_number = int(input('Enter the 2nd number:'))

#Compare the 2 numbers with `>`, `<`, `>=`, `<=`, `==`, and `!=` operators and print the results
print(first_number,'is greater than', second_number, ':', first_number > second_number)
print(first_number,'is less than', second_number, ':', first_number < second_number)
print(first_number,'is greater than or equal to', second_number, ':', first_number >= second_number)
print(first_number,'is less than or equal to', second_number, ':', first_number <= second_number)
print(first_number,'is equal to', second_number, ':', first_number == second_number)
print(first_number,'is not equal to', second_number, ':', first_number != second_number)

