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
print(factorial(0))

def euler(n):
    euler = 0
    for n in range(n + 1):
        euler = 1 / factorial(n)
    return euler
print(euler(5))


def prime(n):
    for i in range (1,10,1):
        if n % i != n: return print('Not a prime number')
    if n == 1 or n == 2: return print('Prime')
prime(1)
prime(2)
prime(3)
prime(4)
prime(5)
prime(7)
prime(8)
prime(9)
