class Mitarbeiter:
    def __init__ (self, vn, nn, str, plz, ort, tel, id):    # Aufgabe 2
        self.vname = vn
        self.nname = nn
        self.str = str
        self.plz = plz
        self.ort = ort
        self.tel = tel
        self.__id = int(id)     # Aufgabe 6

    def __del__ (self):         # Aufgabe 5 -> opt2
        print ("Mitarbeiter gelöscht")

    def set_id (self, val): self.__id = int(val)       # Aufgabe 6 

    def print_adresse (self): print (f"{self.vname} {self.nname}\n{self.str}\n{self.plz} {self.ort}")          # Aufgabe 1

m1 = Mitarbeiter ("Markus", "Maier", "Musterstr. 11", "12345", "Musterhausen", "+49123/1231234", 1) # Aufgabe 3
m1.tel = "123/12341234"     # Aufgabe 4
m1.print_adresse()

del m1      # Aufgabe 5 -> opt1
