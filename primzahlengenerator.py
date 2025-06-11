import math
import time

a = 1_000_000_000_000_000
b = a + 100
primzahlen = []
start = time.time()
for z in range(a,b+1):
    prim = True
    if z <= 1: prim = False
    for i in range(2,int(math.sqrt(z))+1):
        if z % i == 0:
            prim = False
            break
    if prim: primzahlen.append(z)
stop = time.time()

print("Dauer",stop - start)
print("Primzahlliste:",primzahlen)