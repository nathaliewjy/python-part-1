import time as t
import os

for jam in range(23, -1, -1):
    for menit in range(59, -1, -1):
        for detik in range(59, -1, -1):
            print(f"{jam} : {menit} : {detik}")
            t.sleep(1)
            os.system("cls")
