sum = 0
anzahl = int(input("Anzahl Durchläufe: "))

for z in range(1, anzahl+1): sum = sum + z

print("Summe: ",sum)
print("Mittelwert: ",sum/anzahl)