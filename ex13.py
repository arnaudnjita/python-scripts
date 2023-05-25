## Parameterless function
# def my_profession():
#     print('I am a software engineer')
# my_profession()

## Function with parameters
# def about_me(name, address, date_of_birth):
#     print('Hello', name, 'welcome to compudemy')
#     print('You are from', address)
#     print('You were born on the', date_of_birth)
# about_me('Njita', 'Molyko, Buea', '5th of April 2000')

## Function to check if a number is odd or even
# number = int(input('Enter a number: '))
# def check_if_odd_or_even(number):
#     if number % 2 == 0:
#         print(number, 'is even')
#     else:
#         print(number, 'is odd') 
# check_if_odd_or_even(number)

# Get two numbers from the user
num1, num2 = int(input('Enter the first number: ')), int(input('Enter the second number: '))

# Function to check if one number is divisible by another number
def check_divisibility(num1, num2):
    if num1 % num2 == 0:
        print(num1, 'is divisible by', num2)
    else:
        print(num1, 'is not divisible by', num2)

# Call the function       
check_divisibility(num1, num2)