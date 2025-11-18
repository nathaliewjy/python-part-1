buah = ["apel", "semangka", "pisang", "anggur", "mangga"]
print(f"List Awal Buah: {buah}")
print("-" * 30)

# len() : ngitung jumlah elemen dalam list
jumlah = len(buah)
print(f"Jumlah elemen dalam list buah : {jumlah}")
print("-" * 30)

# akses elemen by index
print(f"Buah pertama : {buah[0]}")
print(f"Buah terakhir : {buah[-1]}")

# slicing : ngambil sebagian elemen
print(f"Slicing [1:4] (buah ke-1 s/d sebelum 4) : {buah[1:4]}")
print(f"Slicing [:3] (dari awal s/d sebelum buah ke-3) : {buah[:3]}")
print(f"Slicing [2:] (dari buah ke-2 s/d akhir) : {buah[2:]}")

# nyari apakah elemennya ada di list
if "apel" in buah:
    print("Apel : ada")
else:
    print("Apel : tidak ada")
print("-" * 30)

# ganti elemen by index
buah[0] = "kiwi"
print(f"List setelah diubah : {buah}")

# nambah elemen di akhir list (append)
buah.append("jeruk")
print(f"List setelah append : {buah}")

# nambah elemen di index tertentu (insert)
buah.insert(1, "nanas")
print(f"List setelah insert: {buah}")
print("-" * 30)

# hapus elemen by nama (remove)
if "pisang" in buah:
    buah.remove("pisang")
    print(f"List setelah remove : {buah}")

# hapus elemen terakhir (pop)
buah.pop()
print(f"List setelah pop : {buah}")

# hapus elemen by index (pop by index)
buah.pop(1)
print(f"List setelah pop(1): {buah}")
print("-" * 30)

# looping utk print isi list
print("Isi list buah (for loop) :")
for i in buah:
    print(i, end=", ")
print("\n")

# looping by index (print index & isinya)
print("Isi list buah & indexnya (for loop range len):")
for i in range(len(buah)):
    print(f"Index {i} : {buah[i]}")
print("\n")

# looping while
print("Isi list buah & nomornya :")
i = 0
while i < len(buah):
    print(f"Buah ke-{i+1}: {buah[i]}")
    i += 1
print("-" * 30)

# nyalin list (copy)
buah_copy = buah.copy()
print(f"List asli (buah) : {buah}")
print(f"List copy (buah_copy) : {buah_copy}")

buah_copy.append("delima")
print(f"List buah_copy setelah append : {buah_copy}")

# gabungin list (extend)
buah_baru = ["stroberi", "naga"]
buah.extend(buah_baru)
print(f"List buah setelah diextend sama buah_baru : {buah}")

# gabungin list pake operator +
semua_buah = buah + ["durian", "alpukat"]
print(f"List buah setelah digabung pake operator + : {semua_buah}")

# hapus semua buah
buah.clear()
print(f"List setelah clear : {buah}")
print("-" * 30)