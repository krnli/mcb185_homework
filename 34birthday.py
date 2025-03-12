import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

same_bd = 0
for trial in range(trials):
    calendar = [0] * days
    for person in range(people):
        bd = random.randint(0, days-1)
        calendar[bd] += 1
        if calendar[bd] >= 2: 
            same_bd += 1
            break

print(same_bd/trials)
