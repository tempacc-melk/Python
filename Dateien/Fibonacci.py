x = 0
z = 1
sum = 0

for i in range(1000):
    fz = x + z
    print(fz,end=" ")
    if fz > 4_000_000: break
    if fz < 4_000_000 and fz % 2 == 0: 
        sum = sum + fz
    
    x = z
    z = fz

print("")
print("Total sum:",sum)

# 0+1, 1+1, 1+2, 2+3, 3+5, 5+8, 8+13, 13+21, 21+34, 34+55
# 1  , 1  , 2  , 3  , 5  , 8  , 13  , 21   , 34   , 55
# 1  , 2  , 3  , 5  , 8  , 13 , 21  , 34   , 55   , 89