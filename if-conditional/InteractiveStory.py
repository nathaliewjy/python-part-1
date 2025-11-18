import os

print("\t\tINTERACTIVE STORY PROJECT")

print("-"*80)
nama = input("Sebelum mulai, kasih aku satu nama : ")
print("-"*80)
os.system("cls")

print("-"*80)
print(f"Pada suatu hari, ada seorang pedagang telur bernama {nama}. Ia mempunyai uang sebesar Rp 10.000")
uang = 10000
print("-"*80)

pilih_rute = input(f"Untuk mendapat uang, {nama} harus berjalan menuju pasar. Rute mana yang akan dipilih? (Pilih 1 / 2) ")
print("-"*80)
os.system("cls")

if pilih_rute == "1":
    print("-"*80)
    print(f"{nama} memilih rute {pilih_rute} dan memasuki kawasan perkotaan.")
    print(f"Tiba-tiba, ada seorang pembeli telur.")
    pilih_aksi1 = input("Apa yang akan dilakukan? (Pilih 1 / 2) ")
    print("-"*80)
    os.system("cls")

    if pilih_aksi1 == "1":
        print("-"*80)
        print(f"Aksi {pilih_aksi1} dipilih!")
        print(f"{nama} menawarkan telur dengan diskon. Harga awal telur adalah 5000.")

        harga = 5000

        jumlah_beli = int(input("Jumlah beli : "))
        diskon = int(input("Diskon (1 - 100): "))

        total = jumlah_beli * (harga - (harga * diskon / 100))
        uang += total
        print("-"*80)
        os.system("cls")

        print("-"*80)
        print(f"{nama} menjualnya dengan harga Rp{total}.")
        print(f"Sekarang, ia memegang uang sebesar Rp{uang} dan melanjutkan perjalanannya menuju pasar.")
        print("-"*80)

    elif pilih_aksi1 == "2":
        print("-"*80)
        print(f"Aksi {pilih_aksi1} dipilih!")
        print(f"Pembeli menawar dengan harga rendah.")
        print(f"Akhirnya, {nama} tidak jadi menjualnya dan kembali berjalan menuju pasar.")
        print(f"Jadi, uang yang dipegang sekarang masih Rp{uang}")
        print("-"*80)

elif pilih_rute == "2":
    print("-"*80)
    print(f"{nama} memilih rute {pilih_rute} dan memasuki kawasan pedesaan.")
    print(f"Tiba-tiba, ada seorang kakek tua ingin membeli telur dengan diskon di atas 50%.")
    pilih_aksi2 = input("Apa yang akan dilakukan? (Pilih 1 / 2)")
    print("-"*80)
    os.system("cls")

    if pilih_aksi2 == "1":
        print(f"Aksi {pilih_aksi2} dipilih!")
        print(f"{nama} menerima tawarannya. Harga awal telur adalah 5000")

        harga = 5000

        jumlah_beli = int(input("Jumlah beli : "))
        diskon = int(input("Diskon (50 - 100) : "))

        if diskon < 50:
            print("Kakeknya tidak jadi beli karena diskon harus di atas 50%")
        else:
            total = jumlah_beli * (harga - (harga * diskon / 100))
            uang += total
            print("-"*80)
            os.system("cls")

            print("-"*80)
            print(f"{nama} menjualnya dengan harga Rp{total}.")
            print(f"Sekarang, ia memegang uang sebesar Rp{uang} dan melanjutkan perjalanannya menuju pasar.")
            print("-"*80)

    
    elif pilih_aksi2 == "2":
        print("-"*80)
        print(f"Aksi {pilih_aksi2} dipilih!")
        print(f"Kakek tua menawar dengan harga rendah.")
        print(f"Akhirnya, {nama} tidak jadi menjualnya dan kembali berjalan menuju pasar.")
        print(f"Jadi, uang yang dipegang sekarang masih Rp{uang}")
        print("-"*80)
