i = int(input("Zahl: "))

if i % 2 == 0:
    print(i,"ist gerade")
else:
    print(i,"ist ungerade")

if i < 0:
    print(i,"ist negativ")
elif i == 0:
    print(i,"ist genau 0")
else:
    print(i,"ist positiv")

print("*** Ende des Programms ***")
