merkur = [ 'Merkur', 0.39, 2440, 0]
venus = [ 'Venus', 0.72, 6052, 0]
erde = [ 'Erde', 1.0, 6378, 1]
mars = [ 'Mars', 1.52, 3397, 2]
jupi = [ 'Jupiter', 5.2, 71493, 79]
saturn = [ 'Saturn', 9.54, 60267, 82]
uranus = [ 'Uranus', 19.19, 25559, 27]
neptun = [ 'Neptun', 30.07, 24764, 14]

liste = [ merkur, venus, erde, mars, jupi, saturn, uranus, neptun ]

tabellenname = "Sonnensystem"
print ("-----------------------------------------------")
print (f"|{tabellenname:^45}|")
print ("|---------------------------------------------|")
print ("| Name    |Entf.Sonne (AE)|Radius (km)| Monde |")
print ("|---------+---------------+-----------+-------|")

for i in liste:
    print (f"| {i[0]:7} | {i[1]:9.2f}     | {i[2]:9} | {i[3]:4}  |")

print ("|---------------------------------------------|")