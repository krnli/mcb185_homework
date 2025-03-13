import sys
import math
import mcb185
'''
dna = sys.argv[1]
window = int(sys.argv[2])
entropy = float(sys.argv[3])

fsequence = []
nts = 'ACGT'''
'''
for defline, seq in mcb185.read_fasta(dna):
    for nt in range(len(seq)-window+1):
        if nt == 0:
            for base in seq[nt:nt+window-1]:
                fsequence.append(base)
        counts = [0] * len(nts)
        for base in seq[nt:nt+window]:
            indx = nts.index(base)
            counts[indx] = counts[indx] + 1
        h = 0
        probs = []
        for count in counts:
            prob = count/window
            if prob == 0: continue
            h -= prob * math.log2(prob)
        if h >= entropy: 
            fsequence.append(seq[nt+window-1])
        if h < entropy: 
            for i in range(20):
                fsequence.pop() 
            fsequence.append('N' * window)
    seq_f = ''.join(fsequence)

print(f'>{defline}\n')
for i in range(0, 200, 60):
    print(f'{seq_f[i:i+60]}')'''

# in class example

import sys
import mcb185
import argparse
import math

def entropy(win):
    a = win.count('A')/len(win)
    c = win.count('C')/len(win)
    g = win.count('G')/len(win)
    t = win.count('T')/len(win)
    h = 0
    if a != 0: h += a * math.log2(a)
    if c != 0: h += a * math.log2(c)
    if g != 0: h += a * math.log2(g)
    if t != 0: h += a * math.log2(t)
    return -h

parser = argparse.ArgumentParser(description='DNA entropy filter.')
parser.add_argument('fasta', type=str, help='name of fasta file')
parser.add_argument('--size', type=int,default=10, help='window size [%(default)i]')
parser.add_argument('--entropy', type=float,default=1.4, help='entropy threshold [%(default).2f]')
parser.add_argument('--lower', action='store_true')
parser.add_argument('--wrap', type=int, default=80)
arg = parser.parse_args()



for defline, seq in mcb185.read_fasta(arg.fasta):
    mask = list(seq)
    for i in range(len(seq) - arg.size + 1):
        win = seq[i:i+arg.size]
        if entropy(win) < arg.entropy:
            for j in range(i, i+arg.size):
                if arg.lower:
                    mask[j] = seq[j].lower
                else: mask[j] = 'N'
    print('>',defline, sep='')
    mask = ''.join(mask)
    for i in range(0, len(seq), arg.wrap):
        print(mask[i:i+arg.wrap])
