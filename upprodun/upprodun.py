import sys

nm = []
for line in sys.stdin:
    nm.append(int(line))

n = nm[0] #rooms
m = nm[1] #teams
teams_per_room = int(m/n)
remainder = m%n 
rooms = [teams_per_room for j in range(n)]

for k in range(remainder): 
    rooms[k] += 1
for room in rooms: 
    for k in range(room): 
        print('*', end='')
    print('')
        
