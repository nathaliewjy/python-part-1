import os

softdrink = 10000
coffee = 20000
tea = 15000
juice = 10000
water = 5000

print("\tWelcome to Codingbee Mart")
print("-"*40)
print(f"1. Softdrink | {softdrink}")
print(f"2. Coffee | {coffee}")
print(f"3. Tea | {tea}")
print(f"4. Juice | {juice}")
print(f"5. Mineral water | {water}")
print("-"*40)

minuman = int(input("What do you want to buy? (1-5) "))
jumlah = int(input("How many? "))
os.system("cls")

if minuman == 1:
    minuman = "softdrink"
    pay = softdrink * jumlah
elif minuman == 2:
    minuman = "coffee"
    pay = coffee * jumlah
elif minuman == 3:
    minuman = "tea"
    pay = tea * jumlah
elif minuman == 4:
    minuman = "juice"
    pay = juice * jumlah
elif minuman == 5:
    minuman = "mineral water"
    pay = water * jumlah 

if jumlah > 1:
    print(f"You bought more than 1 {minuman} and got 10% discount")
    pay *= 90/100
    
    if jumlah >= 3:
        print(f"You bought more than 3 {minuman} and got another 10% discount. Total : 20%")
        pay *= 90/100
        
        if jumlah >= 5 and jumlah < 10:
            print(f"You bought more than 5 {minuman} and got another 10% discount. Total : 30%")
            pay *= 90/100
        elif jumlah >= 10:
            print(f"You bought more than 10 {minuman} and got 20% discount. Total : 40%")
            pay *= 80/100

print("-"*40)
print(f"Your total payment is {round(pay)}")
print("Thank you for your purchase!")
print("-"*40)