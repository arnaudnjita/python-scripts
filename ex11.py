# Write a program that takes a list of numbers and returns the sum of all the even numbers in the list.

#Initialize the sum variable
sum = 0
sum1 = 0
numbers = [1,2,3,4,5,6,7,8,9,10]

# Loop through the list of 10 numbers, add all even numbers and assign their sum to the sum variable
for i in numbers:
    if i % 2 == 0:
        sum += i  
print('The sum of all even numbers is:', sum)

# Loop through the list of 10 numbers, add all even numbers and assign their sum to the sum variable
for i in range(1,11):
    if i % 2 == 0:
        sum1 += i  
print('The sum of all even numbers is:', sum)



