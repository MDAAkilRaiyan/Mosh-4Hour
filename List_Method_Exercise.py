# List Method Exercise

list = [22, 25, 78, 78, 45, 22, 36, 5, 6, 45, 22]

for li in list:
    occur = list.count(li)
    for x in range(1, occur):
        list.remove(li)

list.sort()
print(list)
