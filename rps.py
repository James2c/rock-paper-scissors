import random

def main():
    choices = ["rock", "paper", "scissors"]
    player_choice = input("Please enter your choice: rock, paper, or scissors: ").lower()
    computer_choice = random.choice(choices)

    if player_choice == computer_choice:
        print(f"Your choice: {player_choice}")
        print(f"Computer choice: {computer_choice}")
        print("Congratulations, you win!")
    else:
        print(f"Your choice: {player_choice}")
        print(f"Computer choice: {computer_choice}")
        print("Sorry, you lose :(")        



main()