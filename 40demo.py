# in class unit 3 material

dna = 'AGCGCTAGCTACC'
for frame in range(3): # separate codon based on frame
    print(frame, end=' ')
    for i in range(frame, len(dna) - 2, 3):
        print(dna[i: i+3])

for i in range(0, len(dna) - 2, 3): 
    for frame in range(3):
        print(i, dna[i: i+3], end=' ')

# unit 4