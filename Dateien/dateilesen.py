do = open ("testdatei1.txt", "r")

liste = []
zahlenliste = []
for zeile in do:
    liste.append (zeile[:-1])
    if str.isdigit(zeile[:-1]): zahlenliste.append(int(zeile[:-1]))

do.close ()

print("Gesamte Datei:")
for zeile in liste:
    print(zeile)

print()
print("Zahlen")

for zeile in zahlenliste:
    print(zeile)
