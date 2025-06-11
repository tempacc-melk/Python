import time

for i in range(-5,6,2):     # Anfangswert, Abbruchkriterium, Schrittweite (von -5 bis 6 in 2er Schritten)
    print(i,end=" ")        # Ausgabe end= " " kein Zeilenumbruch aber mit Leerzeichen
    time.sleep(0.1)           # Wartezeit (auch als float)

print ("Programmende")

for i in range(0,10_000_000):
    if i % 1_000_000 == 0: print(end="*")

print("")
print("Programmende 2")

for i in range(3):
    print (i)