# Python console mini game using GitHub Copilot 

# import the random module
import random

# create a list of play options
t = ["Rock", "Paper", "Scissors"]

# assign a random play to the computer
computer = t[random.randint(0,2)]

# set player to True    
player = True

while player == True:
    # set player to False
    player = False

    # set player to True
    player = True

    # check for a tie
    if player == computer:
        print("Tie!")

    # check for Rock
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)

    # check for Paper
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
        else:
            print ("You win!", player, "covers", computer)
                  
    # check for Scissors    
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)

    # check for invalid input
    else:
        print("That's not a valid play. Check your spelling!")

    # player was set to True, but we want it to be False so the loop continues
    player = False
    computer = t[random.randint(0,2)]

    # break the loop
    break



    
