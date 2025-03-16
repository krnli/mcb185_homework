# Print the names of any sequences matching the PROSITE pattern "D-K-T-G-T"

import mcb185
import sys
import re       # regular expression

for defline, seq in mcb185.read_fasta(sys.argv[1]):
    if 'DKTGT' in seq: print(defline)
print('--')

for defline, seq in mcb185.read_fasta(sys.argv[1]):
    if re.search('DKTGT', seq): print(defline)
print('--')
# re.search() takes 2 arguments: a pattern and a string
#   pattern = 'DKTGT'
#   string = seq

'''
"D-K-T-G-T" is a subset of a larger PROSITE pattern for P-type ATPases phosphorylation site (PDOC00139). 
The full pattern is: "D-K-T-G-T-[LIVM]-[TI]". 
The character class "[LIVM]" means any one of leucine, isoleucine, valine, or methionine. 
Similarly "[TI]" is a choice of two amino acids. 
We can't use in to make a match to this fuzzy pattern, but we can with regex, which uses the exact same syntax for the character classes we used back in Unit 1 with grep.
'''

for defline, seq in mcb185.read_fasta(sys.argv[1]):
    if re.search('DKTGT[LIVM][TI]', seq): print(defline)
print('--')

# more complex pattern
'''
"C-x(2,4)-C-x(3)-[LIVMFYWC]-x(8)-H-x(3,5)-H". 
This is the pattern for C2H2 zinc-finger proteins (PS00028). 
The "x" stands for any amino acid while the number in parentheses stands for a range. 
"x(2,4)" means 2 to 4 amino acids while "x(3)" means exactly 3

In regular expressions, . means any symbol rather than "x". 
Also, regex uses curly braces for ranges rather than parentheses. 
Therefore "x(2,4)" becomes .{2,4} (re)
'''

for defline, seq in mcb185.read_fasta(sys.argv[1]):
    if re.search('C.{2,4}C.{3}[LIVMFYWC].{8}H.{3,5}H', seq): print(defline)
print('--')

'''
Regular expressions can also extract the text they match. 
Each pair of parentheses is called a match group. 
The example below has only one group, which is the entire pattern.
'''

pat = '(C.{2,4}C.{3}[LIVMFYWC].{8}H.{3,5}H)'
for defline, seq in mcb185.read_fasta(sys.argv[1]):
    m = re.search(pat, seq)     # returns the matched object or false if none matched
    if m: print(m.group(1))