import sys

alphabet = sys.argv[1]
match = sys.argv[2]
mismatch = sys.argv[3]

alph = []
for letter in alphabet:
    alph.append(letter)
header = '  '.join(alph)
print('  ', header)

for letter in alph:
    table = []
    for header in alph:
        if letter == header: table.append(match)
        else: table.append(mismatch)
        line = ' '.join(table)
    print(f'{letter} {line}')

