# Variante 1 - Manuelle Überprüfung
z = int(input("Eingabe: "))

prim = True
if z <= 1: prim = False
for i in range(2,z):
    if z % i == 0:
        prim = False
        break

print(f"Ausgabe: {prim}\n")

# Variante 2 - Automatische Überprüfung
liste = [ 1, 7, 11, 27, 101, 10501, 20610, 1_000_003 ]

for l in liste:
    for m in range(2, liste[-1] + 1):
        if l % m == 0: break

    if l == m: print (l)
