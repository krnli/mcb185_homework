import sys
import math

probs = []
for arg in sys.argv[1:]:
    f = float(arg)
    if f <= 0 or f >= 1: sys.exit('error: not a probability')
    probs.append(float(arg))

total = 0
for p in probs: total += p
if not math.isclose(total, 1.0):
    sys.exit('error: probs must sum to 1.0')

h = 0
for p in probs:
    h -= p * math.log2(p)

print(f'{h:.4f}')


# import sys and math
# check if input is a valid prob
# check if the probs add up to 1
# calculate shannon entropy and print
