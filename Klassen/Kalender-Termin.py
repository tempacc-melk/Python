class Kalender ():
    def __init__ (self, name):
        self.name = name
        self.termine = []

    def hinzu (self, anlass, von, bis):
        self.termine.append (Termin (anlass, von, bis))
        print ("Termin hinzugefügt")

    def kalprint (self):
        print ("\n"+self.name)
        print ("--------------------------------")
        for t in self.termine:
            t.ausgabe ()
 
class Termin ():
    def __init__ (self, anlass, von, bis):
        self.anlass = anlass
        self.von = von
        self.bis = bis

    def ausgabe (self):
        print (f"{self.anlass:20} {self.von:5}-{self.bis:5}")
 
mykal = Kalender ("Tagesplan")
mykal.hinzu ("Essen","12:00","13:00")
mykal.hinzu ("Joggen","15:00","15:30")
mykal.hinzu ("Physiotherapie","18:00","19:30")
mykal.hinzu ("Tagesschau","20:00","20:15")
mykal.kalprint ()
del mykal
