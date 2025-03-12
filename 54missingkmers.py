
import mcb185
import sys
import itertools
import sequence

dna = sys.argv[1]

def missing_kmers(seq, k):
    kmer2count = set() 
    missing_kmer = set()
    for i in range(len(seq) - k + 1):
        kmer = seq[i:i+k]
        if kmer not in kmer2count: kmer2count.add(kmer)
    revseq = sequence.revcomp(seq)
    for i in range(len(revseq) - k + 1):
        kmer = revseq[i:i+k]
        if kmer not in kmer2count: kmer2count.add(kmer)
    for kmer in kmer_set:
        if kmer not in kmer2count: 
            missing_kmer.add(kmer)
    return missing_kmer

k = 8
for defline, seq in mcb185.read_fasta(dna):  
    while True:
        kmer_set = set()
        for nts in itertools.product('ACGT', repeat=k):     # generating all kmers possible
            kmer = ''.join(nts)
            kmer_set.add(kmer)
        missing = missing_kmers(seq, k)
        if len(missing) != 0: break
        k += 1

print(f'Smallest missing k-mer: {k}\nNumber of missing k-mers: {len(missing)}')
    