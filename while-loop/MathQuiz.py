import os
import random as r
import time as t

print("-"*40)
print("Welcome to Math Quiz! Answer the question correctly.")
input("Press enter to continue...")
print("-"*40)
os.system("cls")

score = 0

while score >= 0:
    angka_pertama = r.randint(1,10)
    angka_kedua = r.randint(1,10)
    operator = r.randint(1,4)

    if operator == 1:
        simbol = "+"
        hasil = angka_pertama + angka_kedua
    elif operator == 2:
        simbol = "-"
        hasil = angka_pertama - angka_kedua
    elif operator == 3:
        simbol = "*"
        hasil = angka_pertama * angka_kedua
    else:
        simbol = "/"
        hasil = round((angka_pertama / angka_kedua),2)

    print("-"*40)
    print("Calculate the following problem. Round down number to only 2 decimals")
    # print(angka_pertama,simbol,angka_kedua,"=")
    print(f"{angka_pertama} {simbol} {angka_kedua} = ")

    start = t.time()
    jawaban = float(input("Your answer : "))
    end = t.time() 

    durasi = end - start

    print("Checking your answer...")
    t.sleep(2)

    if jawaban == hasil and durasi > 5:
        print(f"You're correct but you need {durasi} seconds to answer the problem. Game over.")
        print("-"*40)
        break
    elif jawaban == hasil and durasi < 5:
        score += 1
        print(f"You're correct and you need {durasi} seconds to answer the problem. Now, your score is {score}")
        input("Press enter to continue...")
        os.system("cls")
        continue
    else:
        score -= 1
        print(f"You're wrong. The correct answer is {hasil}. Now, your score is {score}")

print(f"Your final score is {score}")


