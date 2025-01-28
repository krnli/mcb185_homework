# Function for Melting Temperature of Oligos

def Tm(A, C, G, T):
   length = A + C + G + T
   if length <= 13: return(A + T) * 2 + (G + C) * 2
   else: return 64.9 + 41 * (G + C - 16.4) / (A + T + G + C)

print (Tm(1, 3, 6, 7), end=' C')
