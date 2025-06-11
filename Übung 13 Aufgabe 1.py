def primetest (z):
    prime = True
    if z <= 1: prime = False
    for i in range(2, int(z**0.5)+1):
        if z % i == 0:
            prime = False
            return prime
    return prime

sum = 0
for i in range(1_000_000):
    if primetest (i): sum = sum + i

print (f"The sum of all prime numbers below 1.000.000 is: {sum}")
