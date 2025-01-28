# tuples

import math

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

""" 
while True:
   print('hello')


i = 0
while True:
    i = i + 1
    print('hey', i)
    if i == 3: break

i = 1
while i < 10:
    print(i)
    i = i + 3
print('final value of i is', i)

for i in range(1, 10, 3):
    print(i)

for i in range(0, 5):
    print(i)

for i in range(5):
    print(i)

basket = 'milk', 'eggs', 'bread'
for thing in basket:
    print(thing)

for i in range(len(basket)):
    print(basket[i])

for i in range(7):
    if i % 2 == 0: print(i, 'is even')
    else:          print(i, 'is odd')

"""

# practice problems

def triangular(n):
    tri = 0
    for i in range(n + 1):
        tri = tri + i
    return tri
print(triangular(1))

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact
print(factorial(5))


def euler(n):
    euler = 0
    while True:
        for i in range(0, n + 1, 1):
            euler = euler + 1 / factorial(i)
        return euler
print(euler(15))

"""
euler = 0
i = 0
while True:
    euler = euler + 1 / factorial(i)
    i = i + 1
    print(euler)
"""


"""
def prime(n):
    for i in range(2, n+1, 1):
        if n / i != 1: return print('not prime')
        else: return print('prime')

prime(1) # prime
prime(2) # prime
prime(3) # prime
prime(4)
prime(5) # prime
prime(7) # prime
prime(8)
prime(9)

"""


