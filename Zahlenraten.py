import random

print("Lassen Sie uns ein Ratespiel spielen, wie viele Zahlen möchten Sie erraten?")
anzahl = int(input("Anzahl: "))
while (anzahl <= 0):
    print("Sie können nicht 0 oder weniger Runden spielen, bitte geben Sie eine neue Zahl ein.")
    anzahl = int(input("Anzahl: "))

def zahlenbereich(von, bis):
    von = int(input("Von: "))
    bis = int(input("Bis: "))
    return von, bis

von = 0
bis = 0

print("In welchen Bereich sollen die Zahlen sein?")
von, bis = zahlenbereich(von, bis)

if abs(von - bis) <= 2:
    print (f"Ihr Zahlenbereich von {von} bis {bis} ist ungültig, bitte geben Sie neue Zahlen ein.")
    von, bis = zahlenbereich(von, bis)

ratezahl = [ random.randint(von,bis) for _ in range(anzahl) ]
gefunden = [ False ] * anzahl

print(f"Erraten Sie die Zahl von {von} bis {bis} - {anzahl}mal. Viel Erfolg!")

counter = 0
versuche = 1
while counter < anzahl:
    vorschlag = int(input(f"Zahl Nr{counter+1} | Versuche {versuche}: "))
    if vorschlag < ratezahl[counter]:
        print("Zu klein!")
        versuche += 1
    elif vorschlag > ratezahl[counter]:
        print("Zu groß!")
        versuche += 1
    else:
        print(f"Treffer Nr{counter+1}")
        gefunden[counter] = True
        counter +=1

print(f"Sie haben gewonnen! Sie haben {versuche}x Versuche gebraucht.")