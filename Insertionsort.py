import time
import random

anzahl = 20_000
liste = [random.randint(1,100_000) for _ in range(anzahl)]

start = time.time();

for i in range(1, len(liste)):
    einzusortierender_wert = liste[i]
    j = i
    while j > 0 and liste[j-1] > einzusortierender_wert:
        liste[j] = liste[j-1]
        j = j - 1
    liste[j] = einzusortierender_wert

stop = time.time();
print(f"Dauer: {stop-start:5.4f}")
print(liste[0:5],liste[-6:-1])
