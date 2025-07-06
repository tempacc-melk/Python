class DemoKlasse:
    def __init__(self, z):
        self.zahl = z
        print (f"Mein Startwert ist: {self.zahl}")

    def zahländern (self, int): self.zahl = int

    def ausgabe(self): print (f"Mein Wert ist: {self.zahl}")

obj1 = DemoKlasse(10)
obj1.zahländern (15)
obj1.ausgabe ()

####################################################################

class Kunde:
    def __init__ (self, v, n, nr):
        self.nr = nr
        self.vorname = v
        self.name = n

    def __del__(self):
        print ("Programm Ende")

    def ausgabe(self):
        print (f"{self.nr:5} {self.name:10} {self.vorname:10}")

k1 = Kunde ("Hans", "Meier", 10001)
k2 = Kunde ("Erna", "Müller", 10002)

k1.ausgabe()
k2.ausgabe()

####################################################################

class Vorlesung:
    def __init__(self, name):       # Konstruktor
        self.bezeichnung = name
        self.__studenten = []
        print("Vorlesung",self.bezeichnung,"angelegt")
 
    def __del__(self):              # Dekonstruktor
        print("Vorlesung gelöscht")
 
    def add(self, student):
        self.__studenten.append(student)
        print(student, "wurde hinzugefügt")
 
    def printstudents(self):
        print(self.__studenten)

vo = Vorlesung ("Test")
vo.add ("Baum Test")

vo.printstudents()
_ = input ("Enter")
