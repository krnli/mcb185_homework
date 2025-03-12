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

middle = num_seq % 2
if middle == 0: 
    seq_len[seq_len/2] 
       
    


print(f'Number of sequences: {num_seq}')
print(f'Mininum length: {min}')
print(f'Maximum length: {max}')
print(f'Mean length: {tot_len/num_seq}')