import random as r

class Geheimzahl: 
    def __init__(self):
        self.__gzahl = 0

    def getZahl (self): return self.__gzahl
    def setZahl (self, zahl): self.__gzahl = int(zahl)

g = Geheimzahl()
g.setZahl (r.randint(0,100_000))
print (g.getZahl())
