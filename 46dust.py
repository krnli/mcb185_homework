import sys
import math
import mcb185

dna = sys.argv[1]
window = int(sys.argv[2])
entropy = float(sys.argv[3])

fsequence = []
nts = 'ACGT'

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
    print(f'{seq_f[i:i+60]}')
