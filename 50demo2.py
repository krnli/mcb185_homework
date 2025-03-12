# in class demo

import mcb185
import sys
import random
import time

'''
names=[]
vals=[]
name2val = {}       # dictionary
with open(sys.argv[1]) as fp:
    for line in fp:
        name, val = line.split()
        name2val[name] = val
#        names.append(name)
#        vals.append(val)'''
'''
for key, val in name2val.items():
    print(key, val)
sys.exit()

print(names[:3])
print(vals[:3])

if 'FIPOEAEPL' in names:
    pos = names.index('FIPOEAEPL')
    print(vals[pos])'''

'''
t0 = time.time()
names = list(name2val.keys())
for i in range(1000):         # doing searches
    token = random.choice(names)
    print(token, name2val[token])
    #pos = names.index(token)
    #val = vals[pos]
    #print(token, pos, val)
t1 = time.time()
print(t1-t0)'''

'''
for i in range(1000000):
    name = random.choices('ABCDEFGHIJKLMOP', k = 9)
    name = ''.join(name)
    val = random.random()
    print(name, val)
'''

'''
k = 4
kmer2count = {}
for defline, seq in mcb185.read_fasta(sys.argv[1]):
    for i in range(len(seq) - k +1):
        kmer = seq[i:i+k]
        if kmer not in kmer2count: kmer2count[kmer] = 0
        kmer2count[kmer] += 1

for kmer, n in kmer2count.items():
    print(kmer, n)
'''

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('file', help='file name')
parser.add_argument('--minchar', type = int, default=29)
arg = parser.parse_args()

with open(arg.file) as fp:
    for line in fp:
        if len(line) >= arg.minchar: print(len(line))