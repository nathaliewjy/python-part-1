angka1 = 0
angka2 = 1
 
while True:
    panjang = int(input("Panjang deret fibonacci (min. 2) : "))

    if panjang > 2:
        break
    else:
        print("Input angka harus lebih besar dari 2!")

print("Deret Fibonacci:")
print(angka1,angka2, end=" ")

counter = 2
# 2 angka pertama udh di print

while counter < panjang:
  next_num = angka1 + angka2
  print(next_num, end=" ")
  angka1 = angka2
  angka2 = next_num
  counter += 1