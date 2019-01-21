import math
import random

# In these cases the 'w' is the marble we are trying to remove
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

# test() handles both replacement and without replacement cases and can take a number of iterations as a parameter
def test(replace, trials):
    results = []
    if(replace):
        for i in range(trials):
            results.append(replacing())
        print("With replacement average: " + str(average(results)) + " draws")

    else:    
        for i in range(trials):
            results.append(noReplacing())
        print("Without replacement average: " + str(average(results)) + " draws")

# Function that returns the average of a set of integers and returns a float
def average(numbers):
    return sum(numbers)/len(numbers)

print("Running With Replacement with 1000000 iterations")
test(True, 1000000) 
print("Running Without Replacement with 1000000 iterations")
test(False, 1000000)