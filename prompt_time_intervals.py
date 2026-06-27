def time_interval_verification ():
    while True:
        try:
            time_interval = int(input("How much time do you want to wait between intervals? (minutes) "))
            if time_interval <= 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    return time_interval