# Ask user if they want to generate a password or not
# If yes, ask for password length
# Generate password then print
# If initial response is no, exit program

import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%^")


def new_password():
    length = int(input(
        "Please indicate how long you would like your password to be? "))
    random.shuffle(characters)
    password = []

    for x in range(length):
        password.append(random.choice(characters))

    random.shuffle(password)

    password = "".join(password)
    print(password)


choice = input("Do you want to create a password? Please select Yes or No: ")
if choice == "Yes":
    new_password()
elif choice == "No":
    print("Goodbye")
    quit()
else:
    print("Invalid selection. Please try again.")
    quit()
