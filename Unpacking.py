# Unpacking - Can be used for both Tuples and List

coordinates = (1, 2, 3)
# Normal Style
x = coordinates[0]
y = coordinates[1]
z = coordinates[2]
print(f"{x} {y} {z}")

# Unpacking Style
m, n, o = coordinates

print(f"{m} {n} {o}")
