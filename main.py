# import randint from random
from random import randint
from hand_art import responses

# Intro:
print("Welcome to ROCK PAPER SCISSORS!")
print("Would you like to play?")

# While game_over:
game_over = True
asked_to_play = 0
while game_over:
    play = input("Type 'Yes' or 'No': ")
    asked_to_play += 1
    if play.lower() != 'yes' and play.lower() != 'no':
        print("That is not a valid input.")
        print("Let's try again...")
        continue
    elif play.lower() == 'no' and asked_to_play == 1:
        print("Are you sure?")
        print("It's a lot of fun.")
        continue
    elif play.lower() == 'no':
        print("Understood.")
        print("Maybe some other time...")
        break
    else:
        print("Great! Let's play...")
        print("Best out of 5")
        game_over = False
# Win counters:
p1_wins = 0
cpu_wins = 0
# While game not won:
while p1_wins + cpu_wins < 5:
    p1_choice = int(input("Type 0 for 'Rock', 1 for 'Paper', or 2 for 'Scissors': "))
    cpu_choice = randint(0, 2)
    # If player out of bounds:
    if p1_choice < 0 or p1_choice >= 3:
        print("Invalid input")
        continue
    # Else player in bounds:
    else:
        print(f"You chose {responses[p1_choice]}")
        print(f"I chose {responses[cpu_choice]}")
    # If both players and cpu pick same response:
    if p1_choice == cpu_choice:
        print("It's a DRAW")
        print(f"The current score is {p1_wins} to you and {cpu_wins} to me.")
        continue
    # If player chooses scissors and cpu chooses rock:
    if p1_choice == 2 and cpu_choice == 0:
        cpu_wins += 1
        print("You LOSE!")
        print(f"The current score is {p1_wins} to you and {cpu_wins} to me.")
        continue
    # If cpu chooses scissors and player chooses rock:
    if cpu_choice == 2 and p1_choice == 0:
        p1_wins += 1
        print("You WIN!")
        print(f"The current score is {p1_wins} to you and {cpu_wins} to me.")
        continue
    # If player chooses higher value than cpu:
    if p1_choice > cpu_choice:
        p1_wins += 1
        print("You WIN!")
        print(f"The current score is {p1_wins} to you and {cpu_wins} to me.")
        continue
    # If cpu chooses higher value than player:
    if cpu_choice > p1_choice:
        cpu_wins += 1
        print("You LOSE!")
        print(f"The current score is {p1_wins} to you and {cpu_wins} to me.")
        continue
if cpu_wins > p1_wins:
    print("\nGame Over.")
    print(f"You lost {p1_wins} to {cpu_wins}")
else:
    print("\nGame Over.")
    print(f"You won {p1_wins} to {cpu_wins}")
