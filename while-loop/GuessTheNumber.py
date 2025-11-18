import os
import random as r

print("-"*40)
print("You have to guess a number to win the game.")
input("Press enter to continue...")
print("-"*40)
os.system("cls")

number = r.randint(1,100)
answer = 0
chance = 10

print(f"You have {chance} chance to guess the number")

while answer != number and chance > 0:

    answer = int(input("Guess from 1 - 100 : "))

    if answer == number:
        print("Your input is right.")
        break
    elif answer > number:
        chance -= 1
        print(f"Your input is too big. Now, your chance is {chance}")
    elif answer < number:
        chance -= 1
        print(f"Your input is too small. Now, your chance is {chance}")

    input("Press enter to continue...")
    os.system("cls")

os.system("cls")

if answer == number:
    print(f"Congratulations. The correct number was {number}")
    print(f"You guessed it in {10 - chance} tries.")
else:
    print(f"You ran out of chances. The correct number was {number}.")

