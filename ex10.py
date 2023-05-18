# Loops in Python

# for loop with strings (print all characters in srting)
name = "Njita"
for i in name:
    print(i)
print("\n")
    
# for loop with range (print 1 to 9)    
for num in range(1,10):
    print(num)
print("\n")
    
# for loop with list (print all items in list)
names = ["Njita", "Njoki", "Njoroge"]
ages = [1, 2, 3, 4, 5]
for i in names:
    print(i)
print("\n")

for i in ages:
    if i == 4:
        print('I\'m at index 4')
    else:
        print('welcome') 
print("\n")

sum = 0
for i in range(1,10):
    sum = sum + i
    print(sum)
print('The sum of the numbers from 1 to 9 is:', sum)
print("\n")

count = 0
while(count < 5):
    count = count + 1   
    print('Hey happiness')
print("\n")

# An infinite loop 
count = 10
while count >= 1:
    print(count)
    count = count - 1
    
for i in range(1,10):
    if i % 2 == 0:
        print(i, 'is an even number')
    else:
        print(i, 'is an odd number')
    
    