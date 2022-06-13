import random

game_options = list("RPS")

def rock_paper_scissors(player,computer):
        if player == "R" and computer == "P":
            return "computer won!! Paper covers Rock"
        elif player == "P" and computer == "R":
            return "player won!! Paper covers Rock"
        elif player == "P" and computer == "S":
            return "computer won!! Scissor cuts Paper"
        elif player == "S" and computer == "P":
            return "player won!! Scissor cuts Paper"
        elif player == "R" and computer == "S":
            return "player won!! Rock breaks Scissor"
        elif player == "S" and computer == "R":
            return "computer won!! Rock breaks Scissor"
        elif player not in game_options:
            return "wrong input"
        elif player == computer:
            return "Tie"


def play ():
    

    player = input("R for rock ,P for Paper,S for scissors : \n").capitalize()
    computer = random.choice(game_options[0:2])


    print(rock_paper_scissors(player,computer))
    player = input("would you like to play again? y/n \n").capitalize()
    if player == "N":
        exit
    elif player == "Y":
        play()
    else:
        player = input("Wrong input. Try again, Enter y/n \n")
print("Rules of the Game: \n" + "Rock vs Paper -> Paper wins \n" + "Rock vs Scissor -> Rock wins \n" + "Paper vs Scissor -> Scissor wins \n")
play()

