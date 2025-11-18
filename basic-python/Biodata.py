import os
print("\t\tBIODATA PROJECT")

print("-"*40)
print("Halo! Saya Ms. Nathalie dari Codingbee Bandung.")
input("Ayo kita kenalan (press enter)...")
print("-"*40)
os.system("cls")

nama = input("Siapa nama kamu? ")
os.system("cls")

tanggal_lahir =  input("Ulang tahunnya kapan? ")
os.system("cls")

jenis_kelamin = input("Laki-laki / perempuan? ")
os.system("cls")

hobi = input("Hobinya apa? ")
os.system("cls")


print("\t\tBIODATA")

print("-"*40)
print("versi print()")
print("-"*40)

print("Halo",nama,"!")
print("Kamu lahir di tanggal", tanggal_lahir)
print("Kamu adalah", jenis_kelamin)
print("Dan hobinya", hobi)
print("Glad to see you here!")

print("-"*40)
print("versi print(f)")
print("-"*40)

print(f"Halo {nama}! Kamu lahir di tanggal {tanggal_lahir}. Kamu adalah {jenis_kelamin}. Dan hobinya {hobi}. Glad to see you here!")
print("-"*40)