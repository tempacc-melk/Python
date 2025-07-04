import random as r

def primtest (z):
    '''
    Prüfe ob eine Zahl eine Primzahl ist\n
    :param zahl: Prüfe ob eine Zahl eine Primzahl ist
    :return Boolean: Gebe den Boolean aus ob True oder False
    '''
    prime = True
    if z <= 1: prime = False
    for i in range (2, int (z**0.5) + 1):
        if z % i == 0:
            prime = False
            return prime
    
    return prime

def primzahlen_bis (n):
    '''
    Gebe die Primzahlen in einer Liste aus\n
    :param zahl: Prüfe Primzahlen bis zahl 'n'
    :return liste: Eine Liste mit allen Primzahlen bis 'n' aus
    '''
    liste = []
    for i in range (2, n + 1):
        if primtest (i):
            liste.append (i)
            print (i)

    return liste

def primzahlen_vonbis (von, bis, limit):
    '''
    Gebe die Primzahlen in einer Liste aus\n
    Beende die Funktion wenn ein 'Limit' erreicht ist\n
    :param zahl,zahl,zahl: Prüfe Primzahlen 'von' 'bis' 'limit'
    :return liste: Eine Liste mit allen Primzahlen 'von' 'bis' mit 'limit' Elementen zurück
    '''
    liste = []
    if bis == None: bis = (von + limit)**2
    for i in range (von, bis + 1):
        if primtest (i):
            liste.append (i)
        if len (liste) == limit:
            break

    return liste

def randomliste (von, bis, zahlen):
    '''
    Erzeuge eine Liste mit Zufallszahlen in einen gewünschten Bereich\n
    :param von,bis,zahlen: Anfangswert, Endwert, Maximale Anzahl der Zahl
    :return liste: Zufallsliste von Zahlen
    '''
    liste = [ r.randint (von, bis) for _ in range (zahlen) ]
    return liste

def ersetzeumlaute (text):
    '''
    Eine Zeile wird auf Umlaute geprüft 'äöüß' und anschließend ersetzt\n
    :param text: Mit Umlaute
    :return text: Ohne Umlaute
    '''
    umlaute = str.maketrans({"Ä" : "Ae", "ä" : "ae", "Ö" : "Oe", "ö" : "oe", "Ü" : "Ue", "ü" : "ue", "ß" : "ss"})
    text = text.translate(umlaute)
    return text
