# Weight Conversion Program

weight = int(input("Weight: "))

unit = input("(L)bs or (K)g: ")

if unit == 'L' or unit == 'l':
    weight = weight * 0.4536
    print(f'You are {weight} Kilograms')
elif unit == 'K' or unit == 'k':
    weight = weight * 2.205
    print(f"You are {weight} Pounds")
else:
    print("Wrong Unit Entered")
