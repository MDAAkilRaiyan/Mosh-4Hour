# List Challenge

numbers = [4254634, 846546, 4654686, 7783456,
           456875, 545454582, 769568769, 316465793, 4653871]

largest = numbers[0]

for li in numbers:
    # print(li)
    if li > largest:
        largest = li
    else:
        largest = largest

print(f"The largest number will be {largest}")
