import random as r

def primtest (z):
    '''
    Prüfe ob eine Zahl eine Primzahl ist\n
    :param zahl: Prüfe ob eine Zahl eine Primzahl ist}n
    :return Boolean: Gebe den Boolean aus ob True oder False
    '''
    prime = True
    if z <= 1: prime = False
    for i in range (2, int(z**0.5)+1):
        if z % i == 0:
            prime = False
            return prime
    
    return prime

def primzahlen_bis(n):
    '''
    Gebe die Primzahlen in einer Liste aus\n
    :param zahl: Prüfe Primzahlen bis zahl 'n'\n
    :return liste: Gebe eine Liste mit allen Primzahlen bis 'n' aus
    '''
    liste = []
    for i in range (2, n + 1):
        if primtest (i):
            liste.append (i)

    return liste


def Insertsort (liste):
    '''
    Sorte eine Liste mittels dem Insertsort Algorithmus\n
    :param liste: Liste die sortiert werden soll\n
    :return liste: Wird aufsteigend sortiert ausgegeben
    '''
    for i in range(1, len(liste)):
        einzusortierender_wert = liste[i]
        j = i
        while j > 0 and liste[j-1] > einzusortierender_wert:
            liste[j] = liste[j-1]
            j = j - 1
        liste[j] = einzusortierender_wert

    return liste

def Bubblesort (liste):
    '''
    Sorte eine Liste mittels dem Bubblesort Algorithmus\n
    :param liste: Liste die sortiert werden soll\n
    :return liste: Wird aufsteigend sortiert ausgegeben
    '''
    for n in range(len(liste), 1, -1):
        for i in range(0, n - 1):
            if liste[i] > liste[i + 1]:
                liste[i], liste[i + 1] = liste[i + 1], liste[i]

    return liste

def randomliste (von, bis, zahlen):
    '''
    Erzeuge eine Liste mit Zufallszahlen\n
    :param von,bis: Anfangswert, Endwert\n
    :param zahlen: Maximale Anzahl der Zahl\n
    :return liste: Zufallsliste von Zahlen
    '''
    liste = [ r.randint (von, bis) for _ in range (zahlen) ]
    return liste
