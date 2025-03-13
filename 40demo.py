# reading files

"""
fp = open(path)
for line in fp:
    do_something_with(line)
fp.close()

with open(path) as fp: # without close statement
    for line in fp:
        do_something_with(line)

"""

# reading compressed files

"""
import gzip
with gzip.open(path, 'rt') as fp:
    for line in fp:
        print(line, end='')
"""

# class demos

'''
# skew
for i in range(len(seq)):
    for j in range(w):
        seq[i+j]

for i in range():
    win = seq[i:i+w]
 
# dust
low complexity = low entropy
H = - sum(pi * log2(pi))
when pi = 0: skip 

# transmembrane
aas have disagreement on whether or not they are hydrphobic or hydrophilic -- kd 
N-term: signal peptide
C-term: also needs hydrophobic region >30aa
create different function outside the len(seq) loop OR create conditional statementst 

# assessment

## color assessment question
limit = 10 
for r in range(limit):
    for g in range(limit):
        for b in range(limit):
            c1 = best_color(r,g,b)      # different methdods of finding the distance
            c2 = optimal_color(r,g,b)
            if c1==c2 and c1 == c3: 

import random
n = 0
colors = []
while True:
    r = random.randint(0, limit -1)
    g = random.randint(0, limit -1)
    b = random.randint(0, limit -1)
    n += 1
    colors.add(r,g,b) # set
    if len(colors) == limit**3: break       # impractical

# make test files
gzip -c ../file | head 20 > new file
'''
import sys
import mcb185

# Assessment practice

'''
#statistics problem 1
fileseq = sys.argv[1]

tot_len = 0
num_seq = 0
seq_len = []
for defline, seq in mcb185.read_fasta(fileseq):
    num_seq += 1
    while num_seq == 1: 
        min = len(seq)
        max = len(seq)
    tot_len += len(seq)
    seq_len.append(len(seq))
    if len(seq) < min: min = len(seq)
    if len(seq) > max: max = len(seq)

# finding median

seq_len.sort()
half = num_seq % 2
if half == 0:   # if there are even number of sequences
    median = seq_len[(num_seq/2) - 1] + seq_len[(num_seq/2)]
if half != 0:
    median = seq_len[(num_seq-1)/2]
       

print(f'Number of sequences: {num_seq}')
print(f'Mininum length: {min}')
print(f'Maximum length: {max}')
print(f'Median length: {median}')
print(f'Mean length: {tot_len/num_seq}')'''

# generate random FASTA files

import random

aas = ['I', 'V', 'L', 'F', 'C', 'M', 'A', 'G', 'T', 'S', 'W', 'Y', 'P', 'H', 'E', 'Q', 'D', 'N', 'K', 'R', '*']

for seqs in range(10):
    seq = ['M']
    while True:
        indx = random.randint(0,20)
        seq.append(aas[indx])
        if aas[indx] == '*': 
            protein = ''.join(seq)
            print(protein)
            break