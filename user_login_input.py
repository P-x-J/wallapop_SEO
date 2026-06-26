import time
import sys

def login():
    # Wait for you to manually accept cookies
    print("⏳ Waiting for you to accept cookies ...")

    time.sleep(5)

    # Now try to find and click the login link
    print("\n⏳ Please log in to your account...")
    print("The program will continue once you're logged in.")

    # Keep checking if user is logged in (wait for page to change after login)
    time.sleep(6)
    # Ask user if they've finished logging in
    while True:
        user_input = input("\nHave you finished logging in? (Yes/No): ").strip().lower()
    
        if user_input in ['yes', 'y']:
            print("✓ Continuing with the program...")
            break
        elif user_input in ['no', 'n']:
            sys.exit("Exit: User did not login")
        else:
            print("❌ Invalid input. Please type 'Yes' or 'No'.")

    # Continue with your program logic here
    print("\n✓ Program proceeding...")
