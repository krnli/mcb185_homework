import sys
import mcb185
import sequence

w = int(sys.argv[2])


# window: A, C, G, T; each nt has a count
# fill the window
# determine the counts for C and G of the window, C counts, G counts
# window[beginning] -> check which letter it is -> go into the counts, either subtrct 1 or do nothing
# right side: grab the index window[end + 1] = seq[index 1 after] -> either add 1 or do nothing
# find the gc counts by g_counts + c_ounts / total 


for defline, seq in mcb185.read_fasta(sys.argv[1]):
    c = 0
    g = 0
    for i in range(w):
        if seq[i] == 'C': c += 1
        if seq[i] == 'G': g += 1
    print(0, (g+c)/w, (g-c)/(g+c))
    for i in range(1, len(seq) - w + 1):
        if seq[i-1] == 'C': c = c - 1
        if seq[i-1] == 'G': g = g - 1
        if seq[i + w - 1] == 'C': c = c + 1
        if seq[i + w - 1] == 'G': g = g + 1
        print(i, (g+c)/w, (g-c)/(g+c))

# practice
"""
seq_window = []

for defline, seq in mcb185.read_fasta(sys.argv[1]):
    for i in range(len(seq) - w + 1):
        if i == 0: 
            initial = seq[i:i+w]
            for nt in initial:
                seq_window.append(nt)
        seq_window.pop(0)
        seq_window.append(seq[i + w - 1])
        print(i, sequence.gc_comp(seq_window), sequence.gc_skew(seq_window))
"""