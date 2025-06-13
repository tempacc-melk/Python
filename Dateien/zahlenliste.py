import statistics

liste = [ 77, 32, 1, 98, 55, 3, 8, 7, 22, 13, 8, 44, 72]

# a)
liste.sort()
print("Liste sortiert:",liste)

# b)
liste.insert(0,0)
liste.append(99)
print("Neue Elemente hinzugefügt, Liste:",liste)

# c)
del liste[0]
del liste[-1]
liste.sort(reverse=True)
print ("Elemenet 0(erstes) und -1(letztes) gelöscht, sortiert (down):",liste)

# d)
print(f"Summe: {sum(liste)} und Mittelwert: {statistics.mean(liste)}")