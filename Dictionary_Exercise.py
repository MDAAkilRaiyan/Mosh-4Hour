# Dictionary Exercise
phone = input("Phone No: ")
digit_mapping = {
    "0": "Zero",
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
}

# My Solution
Phone_Word = ""

for x in phone:
    Phone_Word = Phone_Word + digit_mapping[x] + " "

print(Phone_Word)

# Mosh Solution
Output = ""

for ch in phone:
    Output += digit_mapping.get(ch, "Wrong Input") + " "

print(Output)
