# Name Length Checking

name = input("Please enter your name... ")
name_length = len(name)

if name_length < 3:
    print("Your name must be at least 3 characters long")
elif name_length > 50:
    print("You cannot exceed the 50 character limit")
else:
    print("Name length looks good")
