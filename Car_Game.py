# Car Game
ready = input(">")

if ready.upper() == "HELP":
    print("Start - to start the car")
    print("Stop - to stop the car")
    print("Quit - to exit")
    i = 0
    while (i < 1):
        response = input("> ")
        if response.upper() == "START":
            print("Car Started...Ready to go!")
        elif response.upper() == "STOP":
            print("Car Stopped.")
        elif response.upper() == "QUIT":
            break
        else:
            print("I don't understand that...")
else:
    print("Wrong Input")
