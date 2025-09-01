# List Methods

numbers = [10, 45, 76, 31, 69, 45, 45]
print(f'Original List = {numbers}')

# Method to Add New Items

# Adding at the very End
numbers.append(23)
print(f'Appended List = {numbers}')

# Adding at a certain position
numbers.insert(0, 37)
print(f'Inserted List = {numbers}')

# Method to Remove Items

# To Remove any specific list item
numbers.remove(23)
print(f'Removed List = {numbers}')

# To Remove the very list item
numbers.pop()
print(f'Popped List = {numbers}')


# Method to Check if an Item is in the list

# Index Method - returns the index number of the first occurrence of the target number
print(numbers.index(76))

# in Operator - Returns true or false if any item is available in the list
print(76 in numbers)
print(77 in numbers)

# Method to Check the Number of occurrence of an item in a list
print(f'Total number of 45 in the list is {numbers.count(45)}')

# Method to Sort My List
numbers.sort()
print(f"Sorted List = {numbers}")

# To clear the whole list item
numbers.clear()
print(f'Cleared List = {numbers}')
