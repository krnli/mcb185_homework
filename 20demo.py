# tuples

import math
import random

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
    for i in range(0, n + 1, 1):
            euler = euler + 1 / factorial(i)
    return euler
print(euler(15))


euler = 0
i = 0
while i < 10:
    euler = euler + 1 / factorial(i)
    i = i + 1
    print(euler)


def prime(n):
    if n == 1: return print('Prime')
    for i in range(2, n):
        if n % i == 0: return print('Not prime')
    if n % n == 0: return print('Prime')

def n_choose_k(n, k):
    Q = factorial(n) / (factorial(k) * factorial(n - k))
    return print(Q)


# Pi = 3 + 4/(2x3x4) - 4/(4x5x6) + 4/(6x7x8) - 4/(8x9x10) ...


def pi(i):
    s = 0
    for a in range(1, i+1, 1):
        n1, n2, n3 = range(2*a, 2*a+3, 1) 
        c = 1
        if a % 2 == 0: c = -1
        s = s + c * (4 / (n1 * n2 * n3))
    pi = 3 + s
    return print(pi)
pi(50)
pi(5)


#k: Represents the number of events you are trying to calculate the probability for.
#n: Represents the expected number of events (also called the "rate" or "lambda").
#It is used to model the probability of a certain number of events occurring within a fixed time interval, 
#given that these events occur independently at a constant average rate

def poisson(k, n):
    fact_k = 1
    for i in range(1, k+1):
        fact_k = fact_k * i
    poisson_prob = (n**k) * (math.e** -n) / fact_k
    return print(poisson_prob)


# Random Numbers

for i in range(5):
    r = random.random()
    print(r)

r = random.randint(1,6)
print(r)   

"""
random.seed(1)
print(random.random())
print(random.random())
random.seed(2)
print(random.random())
print(random.random())
random.seed(1)
print(random.random())
print(random.random())
"""

# More Practice


## estimating pi using Monte Carlo methods
"""
n = 0
point = 0
while True:          
    n += 1
    x = random.random()
    y = random.random()
    distance = math.sqrt(x**2 + y**2)
    if distance < 1: point += 1
    ratio = point / n
    print(ratio * 4)
"""
    
big_total = 0
games = 100
for i in range(games):
    threed6 = 0
    for j in range(3):
        r = random.randint(1, 6) 
        threed6 = threed6 + r 
    big_total += threed6
print(big_total/games) # average of 3D6 stats

threed6r1 = 0
for i in range(games):
    for j in range(3):
        r = random.randint(1, 6) 
        if r == 1: 
            for k in range(50):
                r = random.randint(1, 6)
                if r != 1: break
        threed6r1 = threed6r1 + r 
print(threed6r1/games) # average of 3D6r1 stats

threed6x2 = 0
for i in range(games):
    for j in range(3):
        r1 = random.randint(1, 6) 
        r2 = random.randint(1, 6) 
        if r1 > r2: max = r1
        else: max = r2
        threed6x2 = threed6x2 + max
print(threed6x2/games) # average of 3D6x2 stats

big_total = 0
fourD6d1 = 0
for i in range(games):
    min = 6
    for roll in range(4): 
        r = random.randint(1, 6)
        fourD6d1 = fourD6d1 + r
        if r < min: min = r 
    big_total = fourD6d1 - min
print(big_total/games) # average of 4D6d1 stats


# class example: estimating e
"""
e = 0
for i in range(4):
    e += 1 / factorial(i)
    print(e)

e = 0
n = 0
while True:
    e += 1 / factorial(i)
    n += 1
    print(e)
"""

# assessment example

limit = 101
for i in range(1, limit):
    if i % 3 == 0 and i % 5 == 0: print(i, 'Fizzbuzz')
    elif i%3 == 0: print(i, 'Fizz')
    elif i%5 == 0: print(i, 'Buzz')
    else: print(i)

"""
d = 3
pi = 1
n = 1
while True:
    n += 1
    term = 1 / d
    if n % 2 == 0: term = term * -1
    pi += term
    d = d + 2
    print(pi*4)
"""
# halflings death saves
trial = 1000
die = 0
stable = 0
revive = 0

for i in range(trial):
    fail = 0
    success = 0
    for i in range(5):
        r1 = random.randint(1, 20)
        r2 = random.randint(1, 20)
        if r1 > r2: max = r1
        else: max = r2
        if max == 1: fail += 2
        elif max <= 9: fail += 1
        elif max <= 19: success += 1
        else: 
            revive += 1
            break
        if success == 3: 
            stable += 1
            break
        if fail == 3:
            die += 1
            break
print(die/trial, stable/trial, revive/trial)   

d = 3
pi = 1
n = 1
while True:
    n += 1
    term = 1 / d
    if n % 2 == 0: term = term * -1
    pi += term
    d = d + 2
    print(pi*4)
    if math.isclose(3.14159, pi*4): break