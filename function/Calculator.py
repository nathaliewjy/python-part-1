def penjumlahan(angka1, angka2):
    return angka1 + angka2

def pengurangan(angka1, angka2):
    return angka1 - angka2

def perkalian(angka1, angka2):
    return angka1 * angka2

def pembagian(angka1, angka2):
    return angka1 / angka2

def main():
    while True:
        angka1 = int(input("Angka pertama : "))
        angka2 = int(input("Angka kedua : "))
        operator = input("Operator : ")

        if operator == "+":
            hasil = penjumlahan(angka1, angka2)
        elif operator == "-":
            hasil = pengurangan(angka1, angka2)
        elif operator == "*":
            hasil = perkalian(angka1, angka2)
        elif operator == "/":
            hasil = pembagian(angka1, angka2)
        
        print("Hasil : ",hasil)

        ulang = input("Ulang lagi? (y/n) : ")
        if ulang.lower() != "y":
            break

main()
