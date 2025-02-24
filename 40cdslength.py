import sys
import gzip

with gzip.open(sys.argv[1]) as fp:
    for line in fp:
        if line[0] == '#': continue
        words = line.split()
        if words[2] != 'CDS': continue
        beg = int(words[3])
        end = int(words[4])
        print (end - beg - 1)