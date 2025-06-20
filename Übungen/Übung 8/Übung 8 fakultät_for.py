print("for-schleife (Fakultät berechnen)")

n = int(input("Eingabe: "))
fakult = 1
for i in range(1,n + 1):
    fakult = fakult * i

print("Das Ergebnis ist:",fakult)
