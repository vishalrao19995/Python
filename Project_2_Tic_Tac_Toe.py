import random
from random import choice

PS = 0
CS = 0
print("""
                ______________________________
                ||    Rock Paper Scissor    ||
                ______________________________
                ||      You can Type:       ||   
                ||                          ||
                ||  Rock    : R, r, rock    ||
                ||  Scissor : S, s, scissor ||
                ||  Paper   : P, p, paper   ||
                ______________________________""")

# Game Module
# 
#     Generates the Computers choice
#     Takes in players input
#     Shows the choices made by player and computer
#     Sends it to the GAME ENGINE MODULE to get evaluated and stores result in RESULT
#     Prints the Result from WINNER_DECLARE MODULE
#     Updates the score using WINNER_DECLARE MODULE
 

def Game():
    computer = choice(['Rock', 'Paper', 'Scissor'])   
    player = playerinput()
    print(f"""
                ____________________________________________________________
                ||       Player Choice       ||||       Computer Choice     ||
                ||          {player}            ||||           {computer}         ||
                ____________________________________________________________""")
    result = (gameengine(player, computer))
    print(winner_declare(result))
    (scorekeeper((winner_declare(result))))
    
# Player Input Moudle

#     This converts usual expected alternates for the names ROCK, PAPER or SCISSOR
    
    
def playerinput():
    playersel = str(input("Choose :"))
    if playersel in ["Scissor", "S","s", "scissor"]:
        return "Scissor"
    elif playersel in ["Rock", "R","r", "rock"]:
        return  "Rock"
    elif playersel in ["Paper", "P","p", "paper"]:
        return "Paper"  
    
def gameengine(player, computer):

    if (player == "Rock" and computer == "Scissor") or (player == "Scissor" and computer == "Paper") or (player == "Paper" and computer == "Rock"):
            return "P"
           

    elif (computer == "Rock" and player == "Scissor") or (computer == "Scissor" and player == "Paper") or (computer == "Paper" and player == "Rock"):
            return "C"
     
    else:
        return "D"

def winner_declare(result):
    if result == 'P':
        return "Player Wins"
    elif result == 'C':
        return "Computer Wins"
    elif result == 'D':
        return "Its a Draw"

    
def scorekeeper(winner):
    global PS
    global CS
    if winner == 'Player Wins':
        PS += 1
#         print("Player Score = ", PS, "Computer Score", CS)
        print(f"""
                ************************************************************
                **       Player Score       ****       Computer Score     **
                **          {PS}               ****           {CS}                **
                ************************************************************""")

    elif winner == 'Computer Wins':
        CS += 1
        print(f"""
                ************************************************************
                **       Player Score       ****       Computer Score     **
                **          {PS}               ****           {CS}              **
                ************************************************************""")
    elif winner == 'Its a Draw':
        print(f"""
                ************************************************************
                **       Player Score       ****       Computer Score     **
                **          {PS}               ****           {CS}              **
                ************************************************************""")
    
reset = True

while reset == True:
    Game()
    print("Do you want play again say 1 else 0")
    reset  = int(input())
else:
    print("Bye Bye")