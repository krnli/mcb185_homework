import sys
import mcb185

fileseq = sys.argv[1]


letter_code = ['I', 'V', 'L', 'F', 'C', 'M', 'A', 'G', 'T', 'S', 'W', 'Y', 'P', 'H', 'E', 'Q', 'D', 'N', 'K', 'R']
hydropathy_score = [4.5, 4.2, 3.8, 2.8, 2.5, 1.9, 1.8, -0.4, -0.7, -0.8, -0.9, -1.3, -1.6, -3.2, -3.5, -3.5, -3.5, -3.5, -3.9, -4.5]

win_sig = 8  
win_trans = 11
avg_kd_sig = 2.5
avg_kd_trans = 2


def hyd_score(window):
    kd = 0
    for aa in window:
        if aa not in letter_code or aa == 'P': return False
        idx = letter_code.index(aa)
        hyd = hydropathy_score[idx]
        kd += hyd
    return kd/len(window)

name = ''
num_prot = 0
for defline, protein in mcb185.read_fasta(fileseq):
    if not len(protein) > 41: continue
    for i in range(0, 30 - win_sig + 1):
        win = protein[i:i+win_sig]
        kd = hyd_score(win)
        if kd < avg_kd_sig or kd == False: continue
        if kd >= avg_kd_sig: 
            break
    if not kd >= avg_kd_sig: continue
    for i in range(30, len(protein) - win_trans + 1):
        win = protein[i:i+win_trans]
        kd = hyd_score(win)
        if kd < avg_kd_trans or kd == False: continue
        if kd >= avg_kd_trans: 
            break
    if not kd >= avg_kd_trans: continue
    name = defline[:80]
    print(name) 
