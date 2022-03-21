command = "" ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Its already running.")
        else:
            started = True
            print("The car started, ready to go!")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to exit the game
        """)
    elif command == "stop":
        if not started:
            print("Already stopped.")
        else:
            started = False
            print("The car stopped.")
    elif command == "quit":
        break
    else:
        print("I don't know what that is.")

