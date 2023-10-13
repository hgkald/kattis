from math import floor 
import sys 

hint = None 
tries = 0

min_ = 1
max_ = 1000 

guess = 500 
while hint != "correct" and tries < 10: 
    if hint=="higher": 
        min_ = guess+1 
    elif hint=="lower": 
        max_ = guess-1 
    guess = floor((min_+max_)/2)
    print(guess)
    sys.stdout.flush() 

    hint = input().strip() 
    tries += 1

