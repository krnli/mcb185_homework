# tuples

t = 1, 2 
print(t)
print(type(t))

person = 'Steve', 21, 4792.2479 # name, age, yearly income
print(person, type(person))

def midpoint(x1, y1, x2, y2):
    x = (x1 + x2) / 2
    y = (y1 + y2) / 2
    return x, y
print(midpoint(6, 6, 0, 0))

print(midpoint(1, 2, 3, 4))
m = midpoint(1, 2, 3, 4)
mx, my = midpoint(1, 2, 3, 4)
print(mx, my)
print(m[0], m[1])


# while loop

while True:
    print('hello')