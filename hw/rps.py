import random

choices = ["rock", "paper", "scissors"] 

def game_time():
	player_choice = input("Make your choice: rock, paper, or scissors.")
	player_choice = player_choice.lower().strip()
	while player_choice not in choices:
		player_choice = input("Try again: the choices are rock, paper, or scissors.")	
		player_choice = player_choice.lower().strip()
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

game_time()		