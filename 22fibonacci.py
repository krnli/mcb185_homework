n = 0
m = 1

for i in range(1, 9):
    if i == 1: 
        print(n)
        print(m)
    p = n + m
    if i % 2 == 0: m = p
    else: n = p
    print(p)
