import sys
import math
import mcb185

dna = sys.argv[1]
window = int(sys.argv[2])
entropy = float(sys.argv[3])

nts = 'ACGT'

for defline, seq in mcb185.read_fasta(dna):
    dust = list(seq)
    for nt in range(len(seq) - window + 1):
        counts = [0] * len(nts)
        for base in seq[nt:nt+window]:
            indx = nts.index(base)
            counts[indx] = counts[indx] + 1
            h = 0
            for count in counts:
                prob = count/window
                if prob != 0: h -= prob * math.log2(prob)
        if h < entropy: 
            dust[nt:nt+window] = ['N'] * window
    finalseq = ''.join(dust)

print(f'>{defline}\n')
for i in range(0, len(finalseq)-60+1, 60):
    print(f'{finalseq[i:i+60]}')

# in class example
'''
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
        print(mask[i:i+arg.wrap])'''

# Discord example
'''
import sys
import mcb185
import math

w = sys.argv[2]
w = int(w)
entropy_threshold = sys.argv[3]
entropy_threshold = float(entropy_threshold)

    
for defline, seq in mcb185.read_fasta(sys.argv[1]):
    defwords = defline.split()
    newseq = list(seq)
    print(defline)
    for i in range(len(seq) - w + 1):
        window = seq[i:i+w]
        a = window.count('A')
        t = window.count('T')
        c = window.count('C')
        g = window.count('G')
        if a > 0: a_p = a / w
        else: a_p = 0
        if t > 0: t_p = t / w
        else: t_p = 0
        if c > 0: c_p = c / w
        else: c_p = 0
        if g > 0: g_p = g / w
        else: g_p = 0
        h = 0
        for p in [a_p, t_p, c_p, g_p]:
            if p > 0:
                h -= p * math.log2(p)
        if h < entropy_threshold:
            newseq[i:i+w] = ['N'] * w
    string_newseq = ''.join(newseq)
    for i in range(0,300,60):
        print(string_newseq[i:i+60])'''
