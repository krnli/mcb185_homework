import math

limit = 101

for a in range(1, limit):
    for b in range(a+1, limit):
        c = math.sqrt(a**2 + b**2)
        if c % 1 == 0: print (a, b, round(c))
