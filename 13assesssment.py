import math

def distance(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return print(distance)

def valid_probability(p):
    if p <= 1 and p >= 0: return print('Valid')
    return print('Invalid')

def maximum(a, b, c, d):
    max = a
    if max < b: max = b
    if max < c: max = c
    if max < d: max = d
    return print(max)

distance(0, 0, 3, 4)
valid_probability(0.3)
valid_probability(4)
maximum(11, 7, 9, 5)