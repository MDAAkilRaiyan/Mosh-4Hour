# Guessing Game
number = 14
i = 3
j = 0
while i > 0:
    guess = int(input("Guess: "))
    i -= 1
    j += 1
    if (guess == number):
        print("You Guessed Right!!! You Win!!!!")
        break

    elif (guess != number and j <= 2):
        print("You Guessed Wrong. Try Again!!!")


else:
    print("You Couldn't Guess The Number. You Lose.")
