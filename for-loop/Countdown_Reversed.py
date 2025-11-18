import time as t
import os

for jam in range(24):
    for menit in range(60):
        for detik in range(60):
            print(f"{jam} : {menit} : {detik}")
            t.sleep(1)
            os.system("cls")

