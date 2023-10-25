from sys import stdin 

def main():
    n, q = stdin.readline().split()
    people = {} 
    default = 0 

    for line in stdin: 
        vals = line.split() 
        cmd = vals[0]

        if cmd =="SET": 
            i,x = vals[1:]
            people[i] = x
        elif cmd =="RESTART":
            default = vals[1]
            people.clear()
        elif cmd =="PRINT": 
            i = vals[1]
            print(people.get(i, default))

if __name__=='__main__': 
    main()
