def insertsort (liste):
    '''
    Sorte eine Liste mittels dem Insertsort Algorithmus\n
    :param liste: Liste die sortiert werden soll
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
def bubblesort (liste):
    '''
    Sorte eine Liste mittels dem Bubblesort Algorithmus\n
    :param liste: Liste die sortiert werden soll
    :return liste: Wird aufsteigend sortiert ausgegeben
    '''
    for n in range(len(liste), 1, -1):
        for i in range(0, n - 1):
            if liste[i] > liste[i + 1]:
                liste[i], liste[i + 1] = liste[i + 1], liste[i]

    return liste
def mergesort (liste):
    '''
    Sortiert eine Liste mittels dem MergeSort Algorithmus\n
    :param liste: Liste die sortiert werden soll
    :return liste: Wird aufsteigend sortiert ausgegeben
    '''
    if len (liste) > 1:
        mitte = len (liste) // 2
        half1 = liste[0:mitte]
        half2 = liste[mitte:]
        mergesort (half1)
        mergesort (half2)
        i = j = k = 0
        while i < len (half1) and j < len (half2):
            if half1[i] < half2[j]:
                liste[k] = half1[i]
                k += 1
                i += 1
            else:
                liste[k] = half2[j]
                k += 1
                j += 1
        while i < len (half1):
            liste[k] = half1[i]
            i += 1
            k += 1
        while j < len (half2):
            liste[k] = half2[j]
            j += 1
            k += 1

    return liste
