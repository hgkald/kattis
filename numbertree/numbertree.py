def main(): 
    vals = input().split()
    h = int(vals[0])
    n = 2**(h+1)-1 #number of elements in heap

    if len(vals) == 1: 
        print(n)
        return 
    
    i = 1
    for p in vals[1]:
        if p == 'L':
            i = i*2
        elif p == 'R': 
            i = i*2+1
    print(n+1-i)


if __name__=='__main__': 
    main() 
