# Nested Loops Challenge

# Using Simple Arithmetic Operators
numbers = [5, 2, 5, 2, 2]

# for item in numbers:
# print('x' * item)

# Using Nested Loops

print("Below is an 'F' Shape")
for x in numbers:
    stars = ""
    for y in range(x):
        stars += 'x'
    print(stars)


# To Create an L shape

lengths = [1, 1, 1, 1, 5]
print("Below is an 'L' Shape")

for p in lengths:
    asterics = ''
    for r in range(p):
        asterics += 'x'
    print(asterics)
