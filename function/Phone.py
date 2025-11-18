import os
import random

battery = 100
pulsa = 0
tanggal = 1
bulan = 1
tahun = 2025

def showBattery():
    global battery
    battery -= 1
    if battery <= 0:
        os.system("cls")
        print("Low battery!")
        quit()

def header():
    randSignal = random.randint(1,3)
    if randSignal == 1:
        signal = "3G"
    elif randSignal == 2:
        signal = "4G"
    elif randSignal == 3:
        signal = "5G"
    
    showBattery()

    print("{:10}{:>10}{:3}%" .format(signal,"🔋",battery))
    print("-"*25)
    print("Pulsa : ", pulsa)
    print(f"Masa aktif : {tanggal} / {bulan} / {tahun}")

def calculator():
    os.system("cls")
    while True:
        header()

        angka1 = int(input("Angka pertama : "))
        angka2 = int(input("Angka kedua : "))
        operator = input("Operator (+, -, *, /) : ")

        if operator == "+":
            hasil = angka1 + angka2
        elif operator == "-":
            hasil = angka1 - angka2
        elif operator == "*":
            hasil = angka1 * angka2
        elif operator == "/":
            hasil = angka1 / angka2

        print(f"Hasil : {hasil}")

        ulangLagi = input("Ulang lagi? (y/n) ")
        if ulangLagi == "y":
            calculator()
        else:
            os.system("cls")
            main()

def contact(): 
    os.system("cls")
    header()

    print('''Daftar contact :
1. William
2. Saepul
3. Nijar
4. Ghozy
5. Resi
6. Angel
7. Mentari
8. Nathalie''')
    
    input("press enter...")
    os.system("cls")
    main()

def beliPulsa():
    os.system("cls")
    header()

    print("Pilihan pulsa :")
    print("1. 10000")
    print("2. 20000")
    print("3. 30000")
    pilihPulsa = int(input("Pilih pulsa : "))

    global pulsa

    if pilihPulsa == 1:
        pulsa += 10000
    elif pilihPulsa == 2:
        pulsa  += 20000
    elif pilihPulsa == 3:
        pulsa += 30000
    
    print("Selamat. Pulsa kamu bertambah")

    beliLagi = input("Beli lagi? (y/n) ")
    if beliLagi == "y":
        beliPulsa()
    else:
        os.system("cls")
        main()

def beliKuota():
    os.system("cls")
    header()

    print("Pilihan kuota : ")
    print("1. 5GB / 7 hari")
    print("2. 10GB / 14 hari")
    print("3. 15GB / 30 hari")
    pilihKuota = int(input("Pilih kuota :"))

    global tanggal
    global bulan
    global tahun

    if pilihKuota == 1:
        tanggal += 7
        if tanggal > 31 and (bulan == 1 or bulan == 3 or bulan == 5 or bulan == 7 or bulan == 8 or bulan == 10 or bulan == 12):
            tanggal -= 31
            bulan += 1
        elif tanggal > 28 and bulan == 2:
            tanggal -= 28
            bulan += 1
        elif tanggal > 30 and (bulan == 4 or bulan == 6 or bulan == 9 or bulan == 11):
            tanggal -= 30
            bulan += 1

        if bulan > 12:
            bulan = 1
            tahun += 1
    elif pilihKuota == 2:
        tanggal += 14
        if tanggal > 31 and (bulan == 1 or bulan == 3 or bulan == 5 or bulan == 7 or bulan == 8 or bulan == 10 or bulan == 12):
            tanggal -= 31
            bulan += 1
        elif tanggal > 28 and bulan == 2:
            tanggal -= 28
            bulan += 1;
        elif tanggal > 30 and (bulan == 4 or bulan == 6 or bulan == 9 or bulan == 11):
            tanggal -= 30
            bulan += 1

        if bulan > 12:
            bulan = 1
            tahun += 1
    elif pilihKuota == 3:
        tanggal += 30
        if tanggal > 31 and (bulan == 1 or bulan == 3 or bulan == 5 or bulan == 7 or bulan == 8 or bulan == 10 or bulan == 12):
            tanggal -= 31
            bulan += 1
        elif tanggal > 28 and bulan == 2:
            tanggal -= 28
            bulan += 1;
        elif tanggal > 30 and (bulan == 4 or bulan == 6 or bulan == 9 or bulan == 11):
            tanggal -= 30
            bulan += 1

        if bulan > 12:
            bulan = 1
            tahun += 1

    print(f"Selamat. Masa aktif : {tanggal} / {bulan} / {tahun}")

    beliLagi = input("Beli lagi? (y/n) ")
    if beliLagi == "y":
        beliKuota()
    else:
        os.system("cls")
        main()

def main():
    header()

    print("1. Calculator")
    print("2. Contact")
    print("3. Beli pulsa")
    print("4. Beli kuota")
    print("5. Off")
    pilih = int(input("Pilih menu (1-4) : "))

    if pilih == 1:
        calculator()
    elif pilih == 2:
        contact()
    elif pilih == 3:
        beliPulsa()
    elif pilih == 4:
        beliKuota()
    else:
        quit()

main()

    
    

