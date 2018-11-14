import random


print("Rock, Paper, Scissors")
print("=====================")


def play():
    while True:
        user = input("Rock (r), Paper (p) or scissors (s)? ").lower()
        computer = random.choice(["r", "p", "s"])
        if user == computer:
            print("Draw!")
        elif user == "r" and computer == "s":
            print("You win")
        elif user == "r" and computer == "p":
            print("Computer wins")
        elif user == "p" and computer == "r":
            print("You win")
        elif user == "p" and computer == "s":
            print("Computer wins")
        elif user == "s" and computer == "p":
            print("You win")
        elif user == "s" and computer == "r":
            print("Computer wins")
        else:
            print(">> Does not exist")


play()
