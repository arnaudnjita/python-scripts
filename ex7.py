# Exercise:
# Propose a script that checks if a number is divisible by 2.
# If the number is divisible by 2 it should print “hey this number is divisible by 2”  otherwise it should print “hey this number is not divisible by 2”

#Get number from user
num1 = int(input("Enter a number: "))

#Check if the number is divisible by 2 (i.e the remainder is 0)
if (num1 % 2 == 0):
    print(num1, "is divisible by 2")
else:
    print(num1, "is not divisible by 2") 