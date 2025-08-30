# 2D Lists
# Defining a 2D List
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix)

# Accessing 2D List Items
print(matrix[0][0])

# Modifying Matrix
matrix[1][2] = 5.5
print(matrix)
print(matrix[1][2])


# Nested Loops in Matrix
for row in matrix:
    for item in row:
        print(item)
