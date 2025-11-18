import os

print("\tSCHOOL GRADING PROJECT")

print("-"*40)
name = input("Student name : ")
print("-"*40)
os.system("cls")

print("\t\tINPUT THE SCORES")
print("-"*40)
english = float(input("English score : "))
math = float(input("Mathematics score : "))
science = float(input("Science score : "))
mandarin = float(input("Mandarin score : "))
history = float(input("History score : "))
print("-"*40)
os.system("cls")

average = (english + math + science + mandarin + history) / 5

if average >= 90:
    grade = "A"
    feedback = "Excellent!"
elif average >= 80:
    grade = "B"
    feedback = "Good job!" 
elif average >= 70:
    grade = "C"
    feedback = "Keep going!" 
elif average >= 60:
    grade = "D"
    feedback = "Nice try. Improve again!" 
else:
    grade = "E"
    feedback = "Try again next time. Don't give up!"


print("\t\tSCHOOL REPORT")
print("-"*40)
print(f"Name : {name}")
print(f"English score : {english}")
print(f"Math score : {math}")
print(f"Science score : {science}")
print(f"Mandarin score : {mandarin}")
print(f"History score : {history}")

print("-"*40)
print(f"Average score : {average}")
print(f"Grade : {grade}")
print(f"Feedback : {feedback}")
print("-"*40)



