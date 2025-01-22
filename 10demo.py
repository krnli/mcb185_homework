# 10demo.py by Kristine

import math

# Testing #

print("hello, again")   # greeting
print(1.5e-2)           # math

# Math operations #

print(1+1)          # addition
print(1-1)          # subtraction
print(2*2)          # multiplication
print(1/2)          # division
print(2**3)         # exponentiation
print(5//2)         # integer divide
print(5%2)          # integer divide remainder
print(5*(2+1))      # precedence

# Math Functions #

print(abs(-50))                     # absolute value
print(pow(2, 3))                    # x to the power of y
print(round(1.2470153, ndigits=3))  # rounding decimals

print(math.ceil(3.59))      # round x up
print(math.floor(3.59))     # round x down
print(math.log(10))         # x in log base e
print(math.log2(10))        # x in log base 2
print(math.sqrt(4))         # square root of x
print(math.pow(2, 3))       # x to the power of y
print(math.factorial(4))    # factorial of integer n

# Useful integers #

print(math.e) 
print(math.pi)
print(math.inf)
print(math.nan)     # not a number

# Errors #

# print(1/0) # divide by 0 error
# print(math.log(0)) # math domain error
# print(math.sqrt(-1)) # math domain error

# Numbers Aren't Real #

print(0.1 * 1)
print (0.1 * 3)

# Variables #

## Assignment ##

a = 3                       # side a of triangle
b = 4                       # side b of triangle
c = math.sqrt(a**2 + b**2)  # hypotenuse
print(c)

print(type(a), type(b), type(c), sep=', ', end='!\n')    # variable types

# Functions #

def pythagoras(a, b):
    return math.sqrt(a**2 + b**2)

print(pythagoras(a, b))

# Practice #

def circle_area(r):
    return math.pi * r**2

def rectangle_area(w, h):
    return w * h

def circumference(r):
    return 2 * math.pi * r

def sphere_volume(r):
    return (4/3) * math.pi * r**3

def triangle_area(w, h):
    return rectangle_area(w,h) / 2

def F_to_C(t):
    return (t - 32) * (5/9)

def mph_kph(s):
    return s * 1.60934

def od260_dna(a):
    return a * 50

def arithmetic_mean(a, b, c):
    return (a + b +c) / 3

def harmonic_mean(a, b, c):
    return 3 / ((1/a) + (1/b) + (1/c))

def geometric_mean(a, b, c):
    return pow(a*b*c, 1/3)

def distance(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

# Strings #

s = 'hello world'
print(s, type(s))

# Conditionals #

a = 2
b = 3
if a == b:
    print('a equals b')
print(a,b)

def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False
print(is_even(2))
print(is_even(3))

## Boolean ##

c = a == b
print(c)
print(type(c))

## if-elif-else ##

a = 1
b = 3

if a < b:
	print('a < b')
elif a > b:
	print('a > b')
else:
	print('a == b')
print(a,b)

## Chaining ##

if a < b or a > b: print('all things being equal, a and b are not')
if a < b and a > b: print('you are living in a strange world')
if not False: print(True)

## Floating Point Warning ##

a = 0.3
b = 0.1 * 3
if   a < b: print('a < b')
elif a > b: print('a > b')
else:       print('a == b')                     # don't do

print(abs(a - b)) # 5.551115123125783e-17
if abs(a - b) < 1e-9: print('close enough')     # manual

if math.isclose(a, b): print('close enough')    # math function

## String Comparison ##

s1 = 'A'
s2 = 'B'
s3 = 'a'
if s1 < s2: print('A < B')
if s2 < s3: print('B < a')

## Mismatched Type Error ##

a = '1'
s = 'G'
if a < s: print('a < s')
if a > s: print('a > s')
print(type(a))
print(type(s))

# None Type #

def silly(m, x, b):
	y = m * x + b
print(silly(2, 3, 4))

# More Practice #

def is_integer(x):
     if x % 1 == 0: return True
     return False
print(is_integer(2))

def valid_probability(x):
     if x > 0 and x < 1: return 'Valid'
     else: return 'Invalid'
print(valid_probability(1.5))

def molecular_weight_dna(m):
     if m == 'A': return 313.21
     elif m == 'T': return 304.2
     elif m == 'G': return 329.21
     elif m == 'C': return 289.18
     else: return None
print(molecular_weight_dna('T'))

def complement_dna(nt):
     if nt == 'A': return 'T'
     elif nt == 'T': return 'A'
     elif nt == 'G': return 'C'
     elif nt == 'C': return 'G'
     else: return None
print(complement_dna('A'))

# More Practice #

def maximum(a, b, c):
    if a > b and a > c: return print(a)
    elif b > a and b > c: return print(b)
    elif c > a and c > b: return print (c)
maximum(1, 6, 2)

def scores(tP, fP, tN, fN):
     sensitivity = tP / (tP + fN)
     specificity = tN / (tN + fP)
     precision = tP / (tP + fP)
     F1 = (2 * precision * sensitivity) / (precision + sensitivity)
     return print("Sensitivity = ", round(sensitivity, 3), "\nSpecificity = ", round(specificity, 3), "\nF1 = ", round(F1, 3))
     # return print(f'Sensitvity = {sensitivity:.2f}\nSpecificity = {specificity:.2f}\nF1 = {F1:.2f}')
scores(80, 20, 90, 10)

def entropy(A, C, G, T):
    tot = A + C + G + T
    eA, eC, eG, eT = 0, 0, 0, 0
    if A != 0: eA = (A / tot) * math.log2(A / tot)
    if C != 0: eC = (C / tot) * math.log2(C / tot)
    if G != 0: eG = (G / tot) * math.log2(G / tot)
    if T != 0: eT = (T / tot) * math.log2(T / tot)
    entropy = -1 * (eA + eC + eG + eT)
    return print(entropy)
entropy(0,0,0,0)

import random

while True:
     a = random.randint(1, 10)
     b = random.randint(1, 10)
     c = print(a, b, pythagoras(a, b))
