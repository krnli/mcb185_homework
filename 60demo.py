import sys
import argparse
import mcb185
import json

'''
parser = argparse.ArgumentParser()
parser.add_argument('file', help='file name')
arg = parser.parse_args()'''

"""
records = []

me = {'Name': 'Kris', 'Age': 20}

records.append(me)
records.append( {'Name': 'Joe', 'Age': 23})

print(records)      # list of dictionaries
for rec in records:
    print(rec['Name'])

# feature table
# 2 main data types: list or object

'''
list
plist = [1, 'cat', False]

[
    1
    'cat',
    False
]

object
object = {'name': 'kris', 'age':  20}

{
    'name': 'APGI,
    'chrom': '1',
    'start': '20492',
    'end': '21390231',
    'strand': '+'
    'transcripts': [
        [
        'name': 'APGI-1',
        'start': ...,
        'end': ...,
        'exons': [
            [
            'start': ...
            'end': ...
            ]
        ]
    }       # highly structured and nested, how to display? --> JSON file

'''
ft = []

'''
genome = load_genome(sys.argv[1])
for chrom in genome['characteristic']:
    for gene in genome[chrom]:
        for exon in tx:
            print(exon[end] - exon[beg] + 1)
'''
"""

# Unit 6

# Lists of things
print(sys.argv)
print(sys.argv[0])
print(sys.argv[0][3])

d = [
    'hello',
    (3.14, 'pi'),
    [-1, 0, 1],
    {'year': 2000, 'month': 7}
]
print(d[0][4], d[2][2], d[3]['month'])

# Arrays and Matrices

'''
arrays = linear containers where all elements are the exact same type
    constructed with array()
matrices are multi-dimensional arrays
    are rectangular (each dimension has the same number of elements)
    all values are of the same type
'''

# records

'''
record is a data type with various named fields
    list of dictionaries
example:
    oligo = {
        'Name': 'SO116',
        'Length': 18,
        'Sequence': 'ATTTAGGTGACACTATAG',
        'Description': 'SP6 promoter sequencing primer'
    }
catalog = list of records
    catalog = []
    catalog.append(oligo)

'''

def read_catalog(filepath):
    catalog = []
    with open(filepath) as fp:
        for line in fp:
            if line.startswith('#'): continue
            name, length, seq, desc = line.rstrip().split(',')
            record = {
                'Name': name,
                'Length': length,
                'Sequence': seq,
                'Description': desc
            }
            catalog.append(record)
    return catalog
#print(read_catalog(arg.file))


#catalog = read_catalog(arg.file)
'''
for primer in catalog:
    print(primer['Name'], primer['Description'])'''


def Tm(seq):
   A = seq.count('A')
   T = seq.count('T')
   G = seq.count('G')
   C = seq.count('C')
   total = A + T + G + C
   if total <= 13: return (A + T) * 2 + (G + C) * 2
   return 64.9 + 41 * (G + C - 16.4) / (A + T + G + C)
'''
for primer in catalog:
    primer['Tm'] = Tm(primer['Sequence'])
print(catalog)
'''
# Dict of Lists

seq = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGT'
kloc = {}
k = 2
for i in range(len(seq) -k + 1):        # record of kmers and their positions
    kmer = seq[i:i+k]
    if kmer not in kloc: kloc[kmer] = []
    kloc[kmer].append(i)

# Complex data

'''
EXAMPLE
{      
    "locus": "NC_000913",
    "length": 4641652,
    "type": "DNA",
    "definition": "Escherichia coli str. K-12 substr. MG1655, complete...",
    "reference": [
        {
            "authors": "Riley,M., Abe,T., Arnaud,M.B., Berlyn,M.K...",
            "title": "Escherichia coli K-12: a cooperatively...",
            "journal": "Nucleic Acids Res. 34 (1), 1-9 (2006)",
            "pubmed": 16397293
        },
        {
            "authors": "Hayashi,K., Morooka,N., Yamamoto,Y., Fujita,K...",
            "title": "Highly accurate genome sequences of Escherichia...",
            "journal": "Mol. Syst. Biol. 2, 2006 (2006)",
            "pubmed": 16738553
        }
    ]
}'''

# JSON
'''
data exchange standard called JSON (Javascript object notation)
    Double-quotes only
    Boolean values are true and false (lower case instead of title case)
    Trailing commas are not allowed on the last element of a block
    There are no comments
'''

truc = {
    'animals': {'dog': 'woof', 'cat': 'meow', 'pig': 'oink'},
    'numbers': [1.09, 2.72, 3.14],
    'is_complete': False,
}
print(json.dumps(truc, indent=2))       # converts python syntax to JSON 

# Regular Expressions

'''
PROSITE patterns used to analyze protein sequences
EXAMPLES:
    R-G-D means proteins with the peptide "RGD" in them
    X means any amino acid
    [ST]-X-[RK] means S or T followed by any amino acid, followed by R or K
    [ILV](3,5) any mixture of 3 to 5 of these hydrophobic amino acids
    {P} means not proline
    <M means begins with methionine
    >W means ends with tryptophan
similar to grep
'''