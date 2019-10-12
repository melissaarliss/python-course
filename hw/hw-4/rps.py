import random

choices = ["rock", "paper", "scissors"] 

def game_time():
	player_choice = input("Make your choice: rock, paper, or scissors. ").lower().strip()
	while player_choice not in choices:
		player_choice = input("Try again: the choices are rock, paper, or scissors. ").lower().strip()
	print(f"Your choice is {player_choice}.")

	computer_choice = random.choice(choices)
	print(f"The computer's choice is {computer_choice}.")

	player_score = 0
	computer_score = 0

	if player_choice == computer_choice:
		print("It's a tie!")
	elif player_choice == "rock":
		if computer_choice == "paper":
			print("The computer won.")
			computer_score += 1
		else:
			print("You won!")
			player_score += 1	
	elif player_choice == "paper":
		if computer_choice == "scissors":
			print("The computer won.")
			computer_score += 1	
		else:
			print("You won!")
			player_score += 1	
	elif player_choice == "scissors":
		if computer_choice == "rock":
			print("The computer won.")
			computer_score += 1	
		else:
			print("You won!")
			player_score += 1

	print(f"You have {player_score} points and the computer has {computer_score} points.")
	if input(("Want to play again? Enter yes or no. ")).lower().strip() == "yes":
		game_time()
	else:
		print("Goodbye!")

game_time()
