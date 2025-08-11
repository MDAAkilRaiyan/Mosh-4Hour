# String Methods
course = "Python for Noobs"

# Finding Length
print(len(course))

# Making Upper Case (It Copies the Original and Does not change the Original Variable)
print(course.upper())
print(course)

# Making Lower Case (It Copies the Original and Does not change the Original Variable)
print(course.lower())
print(course)

# Making Title Case (It Copies the Original and Does not change the Original Variable)
print(course.title())
print(course)

# Find Method Helps to Find a Particular Character or a Sequence of Characters in a String
# Also we need to remember that "find" method is case sensitive
print(course.find('o'))
print(course.find('Noobs'))

# Replace Method Helps to Replace any character or sequence of character in a String. This also is a Case Sensitive Method
print(course.replace('Noobs', 'SuperNoobs'))
print(course)

# Checking whether any character or sequence of character exists, we do that with 'in' method. This method returns a Boolean value like True or False. Again, a case sensitive method
print('for' in course)
