liste = [100, 500, True, False, "Mark", -1000]

liste.insert(0,52)
liste.append (4231)

print(f"Gesamte Liste:{liste}")
print(f"Anfangswert: {liste[0]}")
print(f"Endwert: {liste[-1]}")
print(f"Von 2 bis 4: {liste[2:4]}")

del liste[3:5]      # Elemente 3-4 in der Liste löschen
del liste[3]        # Element 3 in der Liste löschen

liste.sort()
print(f"Liste sortiert (up):{liste}")
liste.sort(reverse=True)
print(f"Liste sortiert (down):{liste}")