# 1)
liste = [ 5, 2, -3, 4, 1 ]
for n in range(len(liste), 1, -1):
    for i in range(0, n - 1):
        if liste[i] > liste[i + 1]:
            liste[i], liste[i + 1] = liste[i + 1], liste[i]

print(f"1) {liste}")

del liste[:]

# 2) 3) 4)
import time
import random

anzahl = int(input("Anzahl: "))
liste = [random.randint(1,100_000) for _ in range(anzahl)]

start = time.time()
for n in range(len(liste), 1, -1):
    for i in range(0, n - 1):
        if liste[i] > liste[i + 1]:
            temp = liste[i]
            liste[i] = liste[i + 1]
            liste[i + 1] = temp
stop = time.time()

print(f"\n2)-4)Dauer: {stop - start} \nAnzahl: {anzahl} \nErsten 10 Zahlen {liste[:10]}\nLetzen 10 Zahlen {liste[-10:]}")