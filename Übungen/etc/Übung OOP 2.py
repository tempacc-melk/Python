# Aufgabe 1
class Planet:
    def __init__ (self, name, entfernung, radius, monde):
        self.__name = name
        self.entfernung = float (entfernung)
        self.radius = int (radius)
        self.monde = int (monde)

    def ausgabe (self): print (f"{self.__name:6} | {self.entfernung:<10.2f} | {self.radius:<6} | {self.monde:<3}")
    def get_Name (self): return self.__name      

# Aufgabe 2
p1 = Planet ("Merkur", 0.39, 2440, 0)
p2 = Planet ("Venus", 0.72, 6052, 0)
p3 = Planet ("Erde", 1.0, 6378, 1)

# Aufgabe 3
print ("Name   | Entfernung | Radius | Monde")
print ("-------+------------+--------+------")
p1.ausgabe ()
p2.ausgabe ()
p3.ausgabe ()
