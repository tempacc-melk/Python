print("while-schleife (Fakultät berechnen)")

n = int(input("Eingabe: "))
fakult = 1
i = 1
while i <= n:
    fakult = fakult * i
    i+=1

print("Das Ergebnis ist:",fakult)
