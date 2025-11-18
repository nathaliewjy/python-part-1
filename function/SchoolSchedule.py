import os

def schedule(a,b,c,d):
  print(f"07:00-08:30 = {a}")
  print(f"08:30-10:00 = {b}")
  print(f"10:00-11:30 = {c}")
  print(f"13:00-14:30 = {d}")
  input("Press enter to continue...")


while True:
  os.system('cls')
  print("Daily Schedule")
  print('''1.Monday
2.Tuesday
3.Wednesday
4.Thrusday
5.Friday
0.Quit''')
  
  day = int(input("Choose day : "))

  if day == 1:
    schedule("English","Math","History","PE")
  elif day == 2:
    schedule("Science","Social","Computer","Bahasa Indonesia")
  elif day == 3:
    schedule("Accounting","Math","English","Social")
  elif day == 4:
    schedule("Mandarin","Math","History","Chemistry")
  elif day == 5:
    schedule("Art","Art","Computer","PE")
  else:
    quit()
  