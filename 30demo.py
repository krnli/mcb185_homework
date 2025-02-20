import math


# Strings

s = 'hello world'
print(s)

s1 = 'hey "dude"'
s2 = "don't tell me what to do"
print(s1, s2)

print('hey "dude" don\'t tell me what to do')


s = 'hello' + 'world'
polyA = 'A' * 100
print(polyA)
print(s)

print(s.upper())
print(s)

print(s.replace('o', '')) # removes letter o
print(s.replace('o', '').replace('r', 'i')) # removes o and replaces r with i

# String formatting

print(f'{math.pi}')            # does nothing special
print(f'{math.pi:.3f}')        # 3 fixed digits after decimal
print(f'{1e6 * math.pi:e}')    # exponent notation
print(f'{"hello world":>20}')  # right justify with space filler
print(f'{"hello world":.>20}') # right justify with dot filler
print(f'{20:<10} {10}')        # left justify


# Indexes

seq = 'GAATTC'
print(seq[0], seq[1])
print(seq[-1])

for nt in seq:
    print(nt, end='')
print()

for i in range(len(seq)):
    print(i, seq[i])

s = 'ABCDEFGHIJ'
print(s[0:5])
print(s[0:8:2])
print(s[0:5], s[:5])        # both ABCDE
print(s[5:len(s)], s[5:])   # both FGHIJ
print(s, s[::], s[::1], s[::-1])

dna = 'ATGCTGTAA'
for i in range(0, len(dna), 3):
    codon = dna[i:i+3]
    print(i, codon)

# Tuples

tax = 'Homo', 'sapiens', 9606  # construct tuple
print(tax)                       # note the parentheses in the output

print(tax[0])      # index
print(tax[::-1])   # slice

# enumerate() and zip()

nts = 'ACGT'
for i in range(len(nts)):
    print(i, nts[i])

for i, nt in enumerate(nts):
    print(i, nt)

names = ('adenine', 'cytosine', 'guanine', 'thymine')
for i in range(len(names)):
    print(nts[i], names[i])

for nt, name in zip(nts, names):
    print(nt, name)

# Lists

nts = ['A', 'T', 'C']
print(nts)
nts[2] = 'G'
print(nts)

nts.append('C')
print(nts)

last = nts.pop()
print(last)
print(nts)

nts.sort()
print(nts)
nts.sort(reverse=True)
print(nts)

nucleotides = nts
nucleotides.append('C')
nucleotides.sort()
print(nts, nucleotides)

items = list()
print(items)
items.append('eggs')
print(items)

stuff = []
stuff.append(3)
print(stuff)

alph = 'ACDEFGHIKLMPQRSVW'
print(alph)
aas = list(alph)
print(aas)

text = 'good day          to you'
words = text.split()
print(words)

line = '1.41,2.72,3.14'
print(line.split(','))

s = '-'.join(aas)
print(s)
s = ''.join(aas)
print(s)

if 'A' in alph: print('yay')
if 'a' in alph: print('no')

print('index G?', alph.index('G'))
# print('index Z?', alph.index('Z'))

print('find G?', alph.find('G'))
print('find Z?', alph.find('Z'))

# Command Line Data

import sys
print(sys.argv)

i = int('42')
x = float('0.61803')
print(i, x, i * x)

# x = float('hello') error message