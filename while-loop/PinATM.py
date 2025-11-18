import os

correctPin = 1234
counter = 0
success = False

while counter < 3 and not success:
    guessPin = int(input("Your ATM pin : "))
    os.system("cls")
    
    counter += 1

    if guessPin == correctPin:
        success = True
        break
    else:
        print("Wrong pin. Try again!")

if success:
    print("Correct pin! You can use your card.")
else:
    print("Wrong pin. Your card is declined.")
