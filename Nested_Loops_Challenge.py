# Nested Loops Challenge

# Using Simple Arithmetic Operators
numbers = [5, 2, 5, 2, 2]

# for item in numbers:
# print('x' * item)

# Using Nested Loops

for x in numbers:
    stars = ""
    for y in range(x):
        stars += 'x'
    print(stars)
