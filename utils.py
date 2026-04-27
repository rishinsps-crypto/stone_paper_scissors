import random

choices = ["stone", "paper", "scissors"]

def get_computer_choice():
    return random.choice(choices)

def get_user_choice():
    while True:
        user = input("Enter stone/paper/scissors: ").lower()
        if user in choices:
            return user
        else:
            print("❌ Invalid choice! Try again.")