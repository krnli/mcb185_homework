import random

"""
for events:
    0 = neither
    1 = advantage
    2 = disadvantage
"""

def max_min(a, b):
    if a > b: 
        max = a 
        min = b
    else: 
        max = b  
        min = a
    return max, min

def saving_throws(dc):            # playing for 1 game
    print('Difficulty class:', dc)
    event = random.randint(0, 2)
    roll1 = random.randint(1, 20)
    roll2 = random.randint(1, 20) # if needed
    max, min = max_min(roll1, roll2)
    if event == 0: 
        print('Normal throw. \nThrow is', roll1)
        throw = roll1
    if event == 1:  
        print('Advantage. \nThrows are', roll1, roll2)
        throw = max
    if event == 2: 
        print('Disadvantage. \nThrows are', roll1, roll2)
        throw = min
    if throw >= dc: return print('Saved')
    else: return print('Fall in')

saving_throws(15)

# In class example

trials = 100000
sides = 20
for dc in range(5, 16, 5):
    nor = 0
    adv = 0
    dis = 0
    for i in range(trials):
        r1 = random.randint(1, sides)
        r2 = random.randint(1, sides)
        if r1 >= dc: nor += 1
        if r1 >= dc and r2 >= dc: dis += 1
        if r1 >= dc or r2 >= dc: adv += 1
    print(dc, nor/trials, adv/trials, dis/trials)

