import random
import time

mulai = time.time()

dadu = random.randint(1,6)
print("Tunggu 3 detik...")
time.sleep(3)
print(f"Angka dadu yang muncul : {dadu}")

selesai = time.time()

durasi = selesai - mulai
print(f"Kamu butuh waktu {durasi} detik untuk run program ini")