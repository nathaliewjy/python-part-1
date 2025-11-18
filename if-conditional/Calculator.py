import os

print("\tCALCULATOR PROJECT")

print("-"*40)
angka1 = int(input("Angka pertama : "))
operator = input("Operator (+ - * /): ")
angka2 = int(input("Angka kedua : "))
print("-"*40)
os.system("cls")

if operator == "+":
    hasil = angka1 + angka2
elif operator == "-":
    hasil = angka1 - angka2
elif operator == "*":
    hasil = angka1 * angka2
elif operator == "/":
    hasil = angka1 / angka2

print(f"Hasil dari {angka1} {operator} {angka2} adalah {hasil}")