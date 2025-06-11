'''
Diese Datei dient lediglich zum testen
'''
import random as r

def bubblesort (_liste):
    for n in range(len(_liste), 1, -1):
        for i in range(0, n - 1):
            if _liste[i] > _liste[i + 1]:
                temp = _liste[i]
                _liste[i] = _liste[i + 1]
                _liste[i + 1] = temp

    return _liste

def kubik (x=0): return x ** 3

print(kubik(100))

for i in range(1, 16):
    print (f"{i:2} {kubik(i):5}")

anzahl = 5000
liste = [r.randint(1,100_000) for _ in range(anzahl)]
liste = bubblesort(liste)

print(f"Anzahl: {anzahl} \nErsten 5 Zahlen {liste[:5]}\nLetzen 5 Zahlen {liste[-5:]}")