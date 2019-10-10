import random

# While user input invalid,
    # re-ask

# Given a p1 and p2, compare moves.
# IF ...
    # print msg saying p1 has won
# ELIF ...
    # print msg saying p2 has won
# ELSE
    # print msg saying that there's been a tie

player_choice = None
computer_choice = None
choices = ["rock", "paper", "scissors"] 

print("Make your choice: rock, paper, or scissors!")

player_choice = input()
player_choice = player_choice.lower().strip()

# while player_choice != "rock" or "scissors" or "paper":
# 	print("Make your choice: rock, paper, or scissors!")

print(f"Your choice is {player_choice}.")

computer_choice = random.choice(choices)

print(f"The computer's choice is {computer_choice}.")

if player_choice == "rock" and computer_choice == "paper":
	print("The computer won.")
elif player_choice == "rock" and computer_choice == "scissors":
	print("You won!")	
elif player_choice == "scissors" and computer_choice == "paper":
	print("You won!")
elif player_choice == "scissors" and computer_choice == "rock":
	print("The computer won.")	
elif player_choice == "paper" and computer_choice == "rock":
	print("You won!")
elif player_choice == "paper" and computer_choice == "scissors":
	print("The computer won.")	
else:
	print("It's a tie!")	









