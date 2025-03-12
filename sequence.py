# transcription

def transcribe(dna):
    return dna.replace('T', 'U')

# reverse-complement

def revcomp(dna):
    rc = []
    for nt in dna[::-1]:
        if   nt == 'A': rc.append('T')
        elif nt == 'T': rc.append('A')
        elif nt == 'C': rc.append('G')
        elif nt == 'G': rc.append('C')
        else:           rc.append('N')
    return ''.join(rc)

# translation

## only recognizes start and stop codons

def translate(dna):
    aas = []
    for i in range(0, len(dna), 3):
        codon = dna[i:i+3]
        if      codon == 'ATG': aas.append('M')
        elif    codon == 'TAA': aas.append('*')
        elif    codon == 'TAG': aas.append('*')
        elif    codon == 'TGA': aas.append('*')
        else:                   aas.append('X')
    return ''.join(aas)

def translate2(dna):
    codons = ('ATG', 'TAA', 'TAG', 'TGA')
    aminos = 'M***'
    aas = []
    for i in range(0, len(dna), 3):
        codon = dna[i:i+3]
        if codon in codons:
            idx = codons.index(codon)
            aa = aminos[idx]
            aas.append(aa)
        else:
            aas.append('X')
    return ''.join(aas)

def gc_comp(seq):
    return(seq.count('C') + seq.count('G')) / len(seq)

def gc_skew(sequ):
    c = sequ.count('C')
    g = sequ.count('G')
    if c + g == 0: return 0
    return (g - c) / (g + c)