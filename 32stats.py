import sys
import math

# adding CL arguments to list and sorting
number = 0
values = []
for arg in sys.argv[1:]:
    number += 1
    n = float(arg)
    values.append(n)
    values.sort()

# finding max and min

min = values[0]
max = values[len(values)-1]
        
# mean and std

total = 0
variance = 0
N = len(values)

for n in values: total += n
mean = (total / N)
for n in values: 
    variance += (n - mean) ** 2
std = math.sqrt(variance / N)

# median value

for median in values:
    if N % 2 == 0: 
        half = int(N / 2)
        median = (values[half] + values[half-1]) / 2
    if N % 2 != 0:
        half = int((N + 1) / 2)
        median = (values[half-1])

print()
print(values)
print(f'Number of values: {number}')
print(f'Maximun: {max}')
print(f'Minimum: {min}')
print(f'Mean: {mean:.3f}')
print(f'Standard deviation: {std:.3f}')
print(f'Median: {median}')