i1 = int(input("Zahl1: "))
i2 = int(input("Zahl2: "))
i3 = int(input("Zahl3: "))

if i1 == i2 and i2 == i3: print ("Alle Zahlen sind gleich:",i1)
elif i1 < i2 and i1 < i3:
    if i2 < i3: print (i1,i2,i3)
    else: print (i1,i3,i2)
elif i2 < i1 and i2 < i3:
    if i1 < i3: print (i2,i1,i3)
    else: print (i2,i3,i1)
else:
    if i1 < i2: print (i3,i1,i2)
    else: print (i3,i2,i1)
