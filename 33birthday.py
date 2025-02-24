import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])


same_bd = 0
for i in range(trials):
    birthdays = []
    for i in range(people):
        bd = random.randint(0, days-1)
        birthdays.append(bd)
    for day in birthdays:
        count = birthdays.count(day) 
        if count >= 2:     
            same_bd += 1
            break
print(same_bd/trials)

