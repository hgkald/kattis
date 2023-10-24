from sys import stdin 
from collections import defaultdict 

def main():
    n, q = stdin.readline().split()
    people = defaultdict(int) 
    useDefault = defaultdict(lambda:True) 
    default = 0 

    for line in stdin: 
        vals = line.split() 
        cmd = vals[0]

        if cmd =="SET": 
            i,x = vals[1:]
            people[i] = x
            useDefault[i] = False
        elif cmd =="RESTART":
            default = vals[1]
            people.clear()
            useDefault.clear()
        elif cmd =="PRINT": 
            i = vals[1]
            if useDefault[i]: 
                print(default)
            else: 
                print(people[i])


if __name__=='__main__': 
    main()
