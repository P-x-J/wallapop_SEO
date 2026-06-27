def time_interval_verification ():
    while True:
        try:
            time_interval = int(input("How much time do you want to wait between intervals? (minutes)"))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")