import random

# 1 turn game

success = 0
failure = 0
health = 0
turn = 0
"""
while True:
    turn += 1
    if turn == 1: print('Probability of revive:', 1/20)
    roll = random.randint(1, 20)
    print('\nTurn', turn, '\nRoll is:', roll)
    if roll < 10: 
        failure += 1
        print('Failures:', failure)
    if roll >= 10: 
        success += 1
        print('Success:', success)
    if roll == 1: 
        failure += 2
        print('Failures:', failure)
    if roll == 20: 
        health += 1
        print('Revived: +1 health')
    if failure == 3: print('Dead: 3 failures')
    if success == 3: print('Stable: 3 successes')
    if failure == 3 or success == 3 or health == 1: break
"""

# In class example

trial = 1000
die = 0
stable = 0
revive = 0

for i in range(trial):
    fail = 0
    success = 0
    for i in range(5):
        r = random.randint(1, 20)
        if r == 1: fail += 2
        elif r <= 9: fail += 1
        elif r <= 19: success += 1
        else: 
            revive += 1
            break
        if success == 3: 
            stable += 1
            break
        if fail == 3:
            die += 1
            break
print(die/trial, stable/trial, revive/trial)    
        