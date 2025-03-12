import sys
import gzip

count = {}
with gzip.open(sys.argv[1], 'rt') as fp:
    for line in fp:
        if line.startswith('#'): continue
        f = line.split()
        feature = f[2]
        if feature not in count: count[feature] = 0
        count[feature] += 1
    #for f, n in count.items(): print(f, n)

# Composition
'''
count = {}
for nt in seq:  # counting nt in seq
    if nt not in count: count[nt] = 0
    count[nt] += 1'''

# Sorting

for k in sorted(count): print(k,count[k])       # sorts keys of count
