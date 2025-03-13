import random
import math
trials = 10
genome_len = 1000
read_len = 10
coverage = 3
read_counts = int((genome_len/read_len) * coverage)

total = 0

for i in range(trials):
    genome = [0] * genome_len
    for j in range(read_counts):
        position = random.randint(0, (genome_len - read_len + 1))
        for k in range(position, position+read_len-1):
            genome[k] += 1
    uncovered = genome.count(0)
    cov_percent = (genome_len - uncovered)/genome_len * 100
    total += cov_percent

print(total/trials)
print(1-math.e**-coverage)