import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

same_bd = 0
for trial in range(trials):
    calendar = []
    for date in range(days):
        calendar.append(date)
    for person in range(people):
        birthday = random.randint(0, days-1)
        calendar.append(birthday)
        if calendar.count(birthday) == 3: 
            same_bd += 1
            break

print(same_bd/trials)
