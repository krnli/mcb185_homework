# Function for Melting Temperature of Oligos

def Tm(A, C, G, T):
    return 65.9 + 41 * (G + C - 16.4) / (A + T + G + C)

print (Tm(1, 3, 6, 7), end=' C')
