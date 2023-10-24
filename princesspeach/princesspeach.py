from sys import stdin 

def main(): 
    n, y = [int(x) for x in input().split()]
    obstacles = [False]*n 
    found = 0
    for obs in stdin:
        obstacles[int(obs)] = True
    for i, obstacle in enumerate(obstacles): 
        if not obstacle: 
            found += 1
            print(i)
    print('Mario got',n-found, 'of the dangerous obstacles.')


if __name__=='__main__': 
    main() 
