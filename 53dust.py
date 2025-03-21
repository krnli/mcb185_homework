import argparse
import mcb185
import math

parser = argparse.ArgumentParser(description='DNA entropy filter.')
parser.add_argument('file', type=str, help='name of fasta file')
parser.add_argument('-s', '--size', type=int, default=20,
    help='window size [%(default)i]')
parser.add_argument('-e', '--entropy', type=float, default=1.4,
    help='entropy threshold [%(default).3f]')
parser.add_argument('--lower', action='store_true', help='soft mask') # new argument added
arg = parser.parse_args()
print('dusting with', arg.file, arg.size, arg.entropy, arg.lower)


fsequence = []
nts = 'ACGT'
dna = arg.file
window = arg.size
entropy = arg.entropy

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
        else: 
            for i in range(6):
                fsequence.pop() 
            fsequence.append('N' * window)
    seq_f = ''.join(fsequence)

print(f'>{defline}')
for i in range(0, 200, 60):
    print(f'{seq_f[i:i+60]}')
