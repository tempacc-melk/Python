def primetest (z):
    prime = True
    if z <= 1: prime = False
    for i in range(2, int(z**0.5)+1):
        if z % i == 0:
            prime = False
            return prime
    return prime
 
anz = 0
n = 2
while anz < 200:
    if primetest (n):
        anz = anz + 1
        print(f"{n:4}", end=" ")
        if anz % 10 == 0: print()
    n = n + 1