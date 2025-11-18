import os
import random as r

print("-"*40)
print("Welcome to Rock Paper Scissors Game!")
print("-"*40)

mainLagi = "y"

while mainLagi == "y":
    print ('''1. Rock
2. Paper
3. Scissors''')

    player1 = int(input("Your choice : "))
    player2 = r.randint(1,3)

    if player1 == 1:
        choice1 = "rock"
    elif player1 == 2:
        choice1 = "paper"
    elif player1 == 3:
        choice1 = "scissors"

    if player2 == 1:
        choice2 = "rock"
    elif player2 == 2:
        choice2 = "paper"
    elif player2 == 3:
        choice2 = "scissors"


    if player1 == player2:
        print(f"Player 1 {choice1} vs Player 2 {choice2}. Tie!")
    elif (player1 == 1 and player2 == 2) or (player1 == 2 and player2 == 3) or (player1 == 3 and player2 == 1):
        print(f"Player 1 {choice1} vs Player 2 {choice2}. You lose!")
        break
    elif (player1 == 1 and player2 == 3) or (player1 == 2 and player2 == 1) or (player1 == 3 and player2 == 2):
        print(f"Player 1 {choice1} vs Player 2 {choice2}. You win!")
    

    mainLagi = input("Wanna play again? (y/n)")
