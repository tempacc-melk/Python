class Konto:
    def __init__ (self, n):
        self.inhaber = n
        self.__kontostand = 0.0

    def einzahlen (self, betrag):
        self.__kontostand += betrag
        print (f"{betrag}€ wurde eingezahlt. Neuer Kontostand: {self.__kontostand}€")

    def abheben (self, betrag):
        if self.__kontostand < betrag:
            print ("Der Betrag kann nicht abgehoben werden. Kontostand ist nicht ausreichend genug gedeckt.")
        else:
            self.__kontostand -= betrag
            print (f"{betrag}€ wurde abgehoben. Neuer Kontostand: {self.__kontostand}€")

    def get_kontostand (self): return self.__kontostand
    

k1 = Konto ("Fritz Maier")
k1.einzahlen (850.97)
k1.einzahlen (123)
k1.einzahlen (1.42)
print ("Kontostand:", k1.get_kontostand())
k1.abheben (1000)
k1.abheben (500)
