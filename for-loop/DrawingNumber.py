# half pyramid
print("segitiga siku-siku versi pertama")
for i in range(1, 6):
    for j in range(1, i+1):
        print(i, end=" ")
    print()

print()
print()

print("segitiga siku-siku versi kedua")
for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

print()
print()


# inverted half pyramid
print("segitiga siku-siku terbalik kiri")
for i in range(5, 0, -1):
    for j in range(1, i+1):
        print(i, end=" ")
    print()

print()
print()


print("segitiga siku-siku terbalik kanan")
for i in range(1, 6):
    for j in range(1, i):
        print(" ", end=" ")
    for j in range(i, 6):
        print(j, end=" ")
    print()

print()
print()


# number
print("segitiga sama sisi bertambah")
count = 1
for i in range(1, 5):
    for j in range(5 - i):
        print(" ", end="")
    for j in range(1, i+1):
        print(count, end=" ")
        count += 1
    print()

print()
print()


# hollow half pyramid
print("segitiga siku-siku kosong")
for i in range(1, 6):
    for j in range(1, i+1):
        if j == 1 or j == i or i == 5:
            print(j, end=" ")
        else:
            print(" ", end=" ")
    print()

print()
print()


# hollow inverted half pyramid
print("segitiga siku-siku kosong terbalik")
for i in range(5, 0, -1):
    for j in range(1, i+1):
        if i == 5:
            print(j, end=" ")
        elif j == i:
            print(5, end=" ")
        elif j == 1:
            print(6-i, end=" ")
        else:
            print(" ", end=" ")
    print()

print()
print()


# full pyramid 
print("segitiga sama sisi")
for i in range(1, 6):
    for j in range(5-i):
        print(" ", end=" ")

    for j in range(i, 2*i):
        print(j, end=" ")

    for j in range(2*(i-1), i-1, -1):
        print(j, end=" ")

    print()





