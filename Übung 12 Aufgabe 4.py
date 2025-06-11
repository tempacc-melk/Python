def quersumme (n):
    qs = 0
    while (n > 0):
        qs = qs + n % 10
        n = n // 10
    return qs

print (quersumme(12345))
