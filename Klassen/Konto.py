class Konto:
    def __init__ (self, n):
        self.inhaber = n
        self.kontostand = 0.0

    def einzahlen (self, betrag):
        self.kontostand += betrag
        print (f"{betrag}€ wurde eingezahlt. Neuer Kontostand: {self.kontostand}€")

    def abheben (self, betrag):
        if self.kontostand < betrag:
            print ("Der Betrag kann nicht abgehoben werden. Kontostand ist nicht ausreichend genug gedeckt.")
        else:
            self.kontostand -= betrag
            print (f"{betrag}€ wurde abgehoben. Neuer Kontostand: {self.kontostand}€")

    def get_kontostand (self): return self.kontostand
    
class Sparkonto(Konto):
    def zinsen_gutschrift(self, zinssatz):
        zinsen = self.kontostand * zinssatz / 100
        self.kontostand += zinsen
        print (f"Es wurde {zinsen:.2f}€ gutgeschrieben. Neuer Kontostand: {self.kontostand:.2f}€")

k1 = Sparkonto ("Fritz Maier")
k1.einzahlen (850.97)
k1.einzahlen (123)
k1.einzahlen (1.42)
print ("Kontostand:", k1.get_kontostand())
k1.abheben (1000)
k1.abheben (500)

k1.zinsen_gutschrift(4)
