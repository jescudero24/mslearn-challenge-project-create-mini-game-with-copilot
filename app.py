# I want to create a game rock, scissors, paper with the computer that chooses randomly between the three options, and the user who chooses one of the three options.   The program will show the choice of the computer and the user, and will determine who is the winner.
# The program will ask the user if he wants to play again, and will continue until the user decides to stop playing.
# The program will show the number of games played and the number of games won by the user, at the end of the game.
# The program will show the choice of the computer and the user, and will determine who is the winner.
# The program will ask the user if he wants to play again, and will continue until the user decides to stop playing.
# The program will show the number of games played and the number of games won by the user, at the end of the game.
# The program will show the choice of the computer and the user, and will determine who is the winner.

import random   # Import the random module
import os       # Import the os module

#print message about the game to the user, rules of the game and ask if the user wants to play
print("Welcome to the Rock, Scissors, Paper game!")
print("The rules are simple: Rock beats Scissors, Scissors beats Paper and Paper beats Rock.")
print("Do you want to play? (yes/no)")

#initialize variables
user_choice = ""
computer_choice = ""
user_wins = 0
games_played = 0

#function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif user_choice == "rock":
        if computer_choice == "scissors":
            return "You win!"
        else:
            return "Computer wins!"
    elif user_choice == "scissors":
        if computer_choice == "paper":
            return "You win!"
        else:
            return "Computer wins!"
    elif user_choice == "paper":
        if computer_choice == "rock":
            return "You win!"
        else:
            return "Computer wins!" 
        
#function to play the game  
def play_game():
    global user_wins
    global games_played
    global user_choice
    global computer_choice
    user_choice = input("Please enter your choice (rock, scissors, paper): ")
    computer_choice = random.choice(["rock", "scissors", "paper"])
    print("Computer choice: " + computer_choice)
    print(determine_winner(user_choice, computer_choice))
    games_played += 1
    if determine_winner(user_choice, computer_choice) == "You win!":
        user_wins += 1
    print("Games played: " + str(games_played))
    print("Games won: " + str(user_wins))
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again == "yes":
        play_game()
    else:
        print("Thanks for playing!")
        os._exit(0)


#check if the user wants to play
play = input()
if play == "yes":
    play_game()
else:    
    print("Thanks for playing!")
    os._exit(0)

#run the game
play_game()

#end of the program
print("Thanks for playing!")
os._exit(0)


