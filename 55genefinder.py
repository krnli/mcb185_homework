import argparse
import mcb185
import sequence

parser = argparse.ArgumentParser()
parser.add_argument('file', help='file name')
parser.add_argument('--orflen', type = int, default=300)
arg = parser.parse_args()

gff = {}
stop_codons = ['TAG', 'TAA', 'TGA']

def orf_finder(dna, start):
    for i in range(start, len(seq) - 2, 3):
        codon = dna[i:i+3]
        if codon in stop_codons: 
            end = i+3
            break
        else: end = False
    return end

ngene = 0
for defline, seq in mcb185.read_fasta(arg.file):
    defwords = defline.split()
    name = defwords[0]
    for frame in range(3):
        ends = set()
        for j in range(frame, len(seq), 3):
            codon = seq[j:j+3]
            if codon == 'ATG': 
                start = j
                end = orf_finder(seq, start)
                if end in ends or end == False: continue
                if not end-start > arg.orflen: continue
                ends.add(end)
                ngene += 1
                gff[(ngene)] = [name, 'CDS', frame+1, '+', start, end]
        revcomp = sequence.revcomp(seq)
        ends = set()
        for j in range(frame, len(seq), 3):
            codon = revcomp[j:j+3]
            if codon == 'ATG': 
                start = j
                end = orf_finder(revcomp, start)
                if end in ends or end == False: continue
                if not end-start > arg.orflen: continue
                ends.add(end)
                ngene += 1
                gff[(ngene)] = [name, 'CDS', frame+1, '-', start, end]
    
    for key, value in gff.items():
        name = value[0]
        feature = value[1]
        frame = value[2]
        strand = value[3]
        start = value[4]
        end = value[5]
        list = [name, feature, frame, strand, start, end]
        for thing in list:
            print(thing,'\t', end='')
        print()




    
