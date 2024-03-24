from time import sleep
import os

def stylish_print(text, speed=0.05):
    for char in text:
        print(char, end='', flush=True)
        sleep(speed)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def create_account():
    stylish_print("Creating your account...\n")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    stylish_print("Account successfully created!\n")
    return username, password

def login(username, password):
    stylish_print("Logging in...\n")
    entered_username = input("Enter your username: ")
    entered_password = input("Enter your password: ")
    if entered_username == username and entered_password == password:
        stylish_print("Login successful!\n")
        return True
    else:
        stylish_print("Incorrect username or password. Please try again.\n")
        return False

def start_chat():
    stylish_print("Starting depression talk...\n")
    stylish_print("Hello, how are you? I hope you're always happy and healthy.\n")
    stylish_print("Before we start the talk, let me know your name.\n")
    stylish_print("Make some nickname for me, please.\n")

def end_chat():
    stylish_print("Okay, my time was done. See you next time!\n")

def main():
    clear_screen()
    stylish_print("Welcome to the Stylish Chat System!\n", 0.03)
    choice = input("Do you want to create an account? (y/n): ")
    if choice.lower() == 'y':
        username, password = create_account()
    elif choice.lower() == 'n':
        stylish_print("Okay, see you next time!\n")
        return
    else:
        stylish_print("Invalid choice. Exiting...\n")
        return

    while True:
        if login(username, password):
            start_chat()
            # Add conversation logic here
            end_chat()
            break

if __name__ == "__main__":
    main()
