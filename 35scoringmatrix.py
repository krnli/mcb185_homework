import sys

# ABCDEFGHIJKLMNOPQRSTUVWXYZ

alph = sys.argv[1]
match = sys.argv[2]
mismatch = sys.argv[3]

column = []
for letter in alph:
    column.append(letter)
head = '  '.join(column)
print('  ', head)

for letter_row in alph:
    row = [letter_row]
    for letter_column in alph:
        if letter_row == letter_column: row.append(match)
        else: row.append(mismatch)
    row = ' '.join(row)
    print(row)
