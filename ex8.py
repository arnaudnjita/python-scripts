#Write an if statement that asks for the user's name via input() function. If the name is “Acha” make it print "Welcome on board Acha” Otherwise make it print "Good morning Engr. Akum”

#Get name from user
name = str(input("Enter a name: "))

if(name == 'Acha'):
    print('Welcome onboard', name)
else:
    print('Good morning Engr.', name)