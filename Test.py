# Sämtlicher Inhalt dieser Daten dient lediglich zum testen
import meinmodul as mm

print(mm.primzahlen_bis(11))

liste1 = [ 1, 2, 3, 4, 5 ]

liste2 = liste1.copy()
print(liste1)

liste2.append(6)
print ("\nChanged liste 2\n")
print(liste2)

extra = [ 7, 8, 9 ]
print ("\nChanged liste 2\n")
liste2.extend(extra)

print(liste2)