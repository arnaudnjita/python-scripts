# Propose a program to calculate Simple Interest
# Simple Interest = (P x T x R)/100 Where, P is the principal amount T is the time and R is the rate
# Take P, T and R as user inputs.

# Get the principal amount from the user and print it
P = float(input('Enter the principal amount: '))
print('Principal =', P, '\n') #\n is a line break

# Get the time from the user and print it
T = float(input('Enter the time: '))
print('Time =', T, '\n')

# Get the rate from the user and print it
R = float(input('Enter the rate: '))
print('Rate =', R, '\n')

# Calculate the simple interest and print it
simple_interest = (P * T * R)/100
print('The Simple Interest is:', simple_interest)



