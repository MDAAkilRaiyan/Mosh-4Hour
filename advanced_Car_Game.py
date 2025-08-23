# Car Game
ready = input(">")

if ready.upper() == "HELP":
    print("Start - to start the car")
    print("Stop - to stop the car")
    print("Quit - to exit")
    i = 0
    status = 'stopped'
    while (i < 1):
        response = input("> ")
        if response.upper() == "START":
            if status == 'stopped':
                print("Car Started...Ready to go!")
                status = 'started'
            else:
                print("THE CAR IS ALREADY RUNNING!!!!!")

        elif response.upper() == "STOP":
            if status == 'started':
                print("Car Stopped.")
                status = 'stopped'
            else:
                print("THE CAR IS ALREADY STOPPED!!!!!")

        elif response.upper() == "QUIT":
            break
        else:
            print("I don't understand that...")
else:
    print("Wrong Input")
