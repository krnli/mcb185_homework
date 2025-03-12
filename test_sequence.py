import sequence
import mcb185

print(sequence.transcribe('ACGT'))

print(sequence.revcomp('AAAACGT'))

print(sequence.translate('ATGCCCTAA')) # should return MX*
print(sequence.translate2('ATGCCCTAA'))
print(mcb185.translate('ATGCCCTAA'))

s = 'ACGTGGGGGGCATATG'
print(sequence.gc_comp(s))
print(sequence.gc_skew(s), sequence.gc_skew(sequence.revcomp(s)))
