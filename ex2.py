import random

n = 0
above = 0
below = 0

while True:
    n += 1
    x = random.random()
    y = random.random()
    if y > x**2: above += 1 
    else: below += 1
    if below > 0: print(f'parabola ratios: {above/below}, {above/n}, {below/n}')
