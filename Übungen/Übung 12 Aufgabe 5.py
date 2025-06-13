def zukunftswert (betrag, jahre, jahreszinsatz):
    endbetrag = betrag
    for i in range (1, jahre + 1):
        endbetrag = endbetrag + endbetrag * jahreszinsatz / 100
    return endbetrag

print (f"{zukunftswert(1_000, 15, 4.95):.2f}")