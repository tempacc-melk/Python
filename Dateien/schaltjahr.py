j = int(input("Jahreszahl eingeben>"))

if j % 400 == 0: schaltjahr = True
elif j % 100 == 0: schaltjahr = False
elif j % 4 == 0: schaltjahr = True
else: schaltjahr = False

print ("Prüfung der Jahreszahl ist abgeschlossen!")

if schaltjahr: print (j,"ist ein Schaltjahr")
else: print (j,"ist kein Schaltjahr\n")
