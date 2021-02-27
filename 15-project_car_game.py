command = ""
car_started = False

while True:
    command = input("> ").lower()

    if command == "start":
        if car_started:
            print("Car already started!")
        else:
            car_started = True
            print("Car started...Ready to go!")
    elif command == "stop":
        if not car_started:
            print("Car already stopped!")
        else:
            car_started = False
            print("Car stopped.")
    elif command == "help":
        print("""start - to start the car \nstop - to stop the car \nquit - to exit""")
    elif command == "quit":
        break
    else:
        print("I don't understand that...")
