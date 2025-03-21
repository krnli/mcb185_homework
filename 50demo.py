
# Sets
## sets are mutable containers, all elements are unieuq and the elements unordered

s = {'A', 'C', 'G'}
print(s)        # not ordered

s.add('T') # to add to a set
print(s)

s.add('A') # doesnt do anything
print(s)

#print(s[2]) generates error because order in a set is random

# Dictionariese
## dictionaries are list a list but its indices are strings

d = dict()
d = {'dog': 'woof', 'cat': 'meow'}  # key:value pair
print(d)
print(d['cat']) # access a dictionary 
d['pig'] = 'oink' # add to a dictionary
d['cat'] = 'mew' # change value of an item using its key
del d['cat']    # delete an item
# print(d['rat']) error because not in dictionary
if 'dog' in d: print(d['dog'])  # check if a key exists

# Iteration
## can use 'for' loop over the keys to iterate through
## to get specific element, use the key index

for key in d: print(f'{key} says {d[key]}')
for k, v in d.items(): print(k, 'says', v)
print(d.keys(), d.values(), list(d.values()))

# Iteration/k-mer

import itertools
for nts in itertools.product('ACGT', repeat=2):
    print(nts)

import random
for i in range(3): 
    kmer = ''.join(random.choices('ACGT', k=2))
    print(kmer)