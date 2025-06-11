# Fiktive Preise
a1 = [ "Nintendo Switch", 309.98 ]
a2 = [ "Sony Playstation 5", 430.99 ]
a3 = [ "Nintendo Switch 2", 499.99 ]
a4 = [ "Microsoft XBox", 450 ]

art = [ a1, a2, a3, a4 ]
art.sort(key=lambda x: x[1])

print("|----------------------|---------|")
print("| Artikel              | Preis   |")
print("|----------------------|---------|")
for e in art:
    print (f"| {e[0]:20} |{e[1]:7.2f}€ |")

print("|----------------------|---------|")
