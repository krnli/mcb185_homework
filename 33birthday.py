import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

birthdays = []
for i in range(people):
    bd = random.randint(0, days)
    birthdays.append(bd)

same_birthdays = 0
for thing in birthdays:
    for thing in birthdays[thing+1:]: same_birthdays += 1

print(same_birthdays/trials)