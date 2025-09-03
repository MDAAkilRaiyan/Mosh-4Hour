# List Method Exercise

# This is My Solution
list = [22, 25, 78, 78, 45, 22, 36, 5, 6, 45, 22]

for li in list:
    occur = list.count(li)
    if occur > 1:
        for x in range(1, occur):
            list.remove(li)


list.sort()
print(list)


# This is Mosh's Solution
duplicates = [1, 2, 3, 1, 2, 3, 1, 2, 3]
originals = []
for duplicate in duplicates:
    if duplicate not in originals:
        originals.append(duplicate)

print(originals)
