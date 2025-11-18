print("kotak")
for i in range(0, 5):
    for j in range(0, 5):
        print("*", end=" ")
    print()

print()
print()


print("segitiga siku-siku kiri")
for i in range(0, 5):
    for j in range(0, i+1):
        print("*", end=" ")
    print()

print()
print()


print("segitiga siku-siku kanan")
for i in range(0, 5):
    for j in range(i, 5):
        print(" ", end=" ")
    for j in range(0, i+1):
        print("*", end=" ")
    print()

print()
print()


print("segitiga siku-siku terbalik kiri")
for i in range(0, 5):
    for j in range(i, 5):
        print("*", end=" ")
    print()

print()
print()


print("segitiga siku-siku terbalik kanan")
for i in range(0, 5):
    for j in range(0, i):
        print(" ", end=" ")
    for j in range(i, 5):
        print("*", end=" ")
    print()

print()
print()


print("segitiga sama sisi")
for i in range(1, 6):
    for j in range(i, 6):
        print(" ", end="")
    for j in range(1, i):
        print("*", end="")
    for j in range(1, i+1):
        print("*", end="")
    print()

print()
print()


print("diamond")
for i in range(1, 6):
    for j in range(i, 6):
        print(" ", end="")
    for j in range(1, i):
        print("*", end="")
    for j in range(1, i+1):
        print("*", end="")
    print()
for i in range(0, 6):
    for j in range(1, i+1):
        print(" ", end="")
    for j in range(i, 5):
        print("*", end="")
    for j in range(i, 6):
        print("*", end="")
    print()
    
print()
print()


print("trapesium")
for i in range (2,6):
    #spasi
    for j in range (i,6):
        print(" ", end="")
    #segitiga (kiri)
    for j in range (1,(i + 1)):
        print("*", end="")
    #segitina (kanan)
    for j in range (1,i):
        print("*", end="")
    print()

print()
print()


print("jajar genjang")
for i in range(5):
    #spasi
    for j in range (5 - i - 1):
        print(" ", end="")
    #square
    for j in range(5):
        print("*", end="")
    print()

print()
print()


print("heart")
for i in range(1, 4):
    for j in range(0, 3-i):
        print(" ", end="")
    for j in range(1, i+1):
        print("*", end=" ")
    for j in range(0, 3-i):
        print(" ", end=" ")
    for j in range(1, i+1):
        print("*", end=" ")
    print()
for i in range(1, 7):
    for j in range(1, i+1):
        print(" ", end="")
    for j in range(i, 6):
        print("*", end=" ")
    print()    

print()
print()


print("trapesium")
for i in range (2,6):
    #spasi
    for j in range (i,6):
        print(" ", end="")
    #segitiga (kiri)
    for j in range (1,(i + 1)):
        print("*", end="")
    #segitina (kanan)
    for j in range (1,i):
        print("*", end="")
    print()

print()
print()


print("jajar genjang")
for i in range(5):
    #spasi
    for j in range (5 - i - 1):
        print(" ", end="")
    #square
    for j in range(5):
        print("*", end="")
    print()

print()
print()


print("heart")
for i in range(1, 4):
    for j in range(0, 3-i):
        print(" ", end="")
    for j in range(1, i+1):
        print("*", end=" ")
    for j in range(0, 3-i):
        print(" ", end=" ")
    for j in range(1, i+1):
        print("*", end=" ")
    print()
for i in range(1, 7):
    for j in range(1, i+1):
        print(" ", end="")
    for j in range(i, 6):
        print("*", end=" ")
    print()    

print()
print()



