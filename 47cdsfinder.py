import sys
import mcb185
import sequence


fileseq = sys.argv[1]
aalength = int(sys.argv[2])


codons = ['TTT', 'TTC', 'TTA', 'TTG', 'TCT', 'TCC', 'TCA', 'TCG', 'TAT', 'TAC', 'TAA', 'TAG', 'TGT', 'TGC', 'TGA', 'TGG', 'CTT', 'CTC', 'CTA', 'CTG', 'CCT', 'CCC', 'CCA', 'CCG', 'CAT', 'CAC', 'CAA', 'CAG', 'CGT', 'CGC', 'CGA', 'CGG', 'ATT', 'ATC', 'ATA', 'ATG', 'ACT', 'ACC', 'ACA', 'ACG', 'AAT', 'AAC', 'AAA', 'AAG', 'AGT', 'AGC', 'AGA', 'AGG', 'GTT', 'GTC', 'GTA', 'GTG', 'GCT', 'GCC', 'GCA', 'GCG', 'GAT', 'GAC', 'GAA', 'GAG', 'GGT', 'GGC', 'GGA', 'GGG']
aas = ['F', 'F', 'L', 'L', 'S', 'S', 'S', 'S', 'Y', 'Y', '*', '*', 'C', 'C', '*', 'W', 'L', 'L', 'L', 'L', 'P', 'P', 'P', 'P', 'H', 'H', 'Q', 'Q', 'R', 'R', 'R', 'R', 'I', 'I', 'I', 'M', 'T', 'T', 'T', 'T', 'N', 'N', 'K', 'K', 'S', 'S', 'R', 'R', 'V', 'V', 'V', 'V', 'A', 'A', 'A', 'A', 'D', 'D', 'E', 'E', 'G', 'G', 'G', 'G']

def orf_finder(dna, frame):
    prot_count = 0
    for i in range(frame, len(seq) - 2, 3):
        codon = dna[i:i+3]
        if codon != 'ATG': continue
        aas_seq = []
        for j in range(i, len(seq) - 2, 3):
            codon = dna[j:j+3]
            idx = codons.index(codon)
            aas_seq.append(aas[idx])
            if aas[idx] == '*': 
                protein = ''.join(aas_seq)
                if len(protein) >= aalength:
                    print(f'>NC_000913.3-prot-{prot_count}\n{protein}')
                    prot_count += 1
                break
    return 
        

for defline, seq in mcb185.read_fasta(fileseq):
    for i in range(3):  
        frame = i
        orf_finder(seq, i)
        orf_finder(sequence.revcomp(seq), i) 