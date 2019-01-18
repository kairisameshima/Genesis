import math
import random
bag = ['w', 'b', 'a', 'c', 'd', 'e']

def noReplacing():
    pool = ['w', 'b', 'a', 'c', 'd', 'e']
    counter = 0
    found = False
    while (not found):
        ball = random.choice(pool)
        counter +=1
        if(ball != 'w'):
            pool.remove(ball)
        else:
            found = True
    return counter

def replacing():
    pool = ['w', 'b', 'a', 'c', 'd', 'e']
    counter = 0
    found = False
    while (not found):
        ball = random.choice(pool)
        counter +=1
        if(ball == 'w'):
            found = True
    return counter

def test(replace, trials):
    results = []

    if(replace):
        for i in range(trials):
            results.append(replacing())
        print(average(results))

    else:    
        for i in range(trials):
            results.append(noReplacing())
        print(average(results))



def average(numbers):
    return sum(numbers)/len(numbers)

test(True, 1000000)
test(False, 1000000)