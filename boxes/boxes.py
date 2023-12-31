from collections import deque
import sys

class Node: 
    def __init__(self, value, parent): 
        self.id = value 
        #self.parent = parent
        self.children = []

class Forest:
    def __init__(self): 
        self.root = Node(0, None) 
        self.nodes = {0: self.root}

    def add_node(self, parentid, nodeid):
        #print("Adding node. Parent:", parentid, "Child:", nodeid)
        if parentid not in self.nodes: 
            parent = Node(parentid, None) 
            self.nodes[parentid] = parent
        else: 
            parent = self.nodes[parentid] 

        if nodeid not in self.nodes: 
            node = Node(nodeid, parent)
            self.nodes[nodeid] = node
        else: 
            node = self.nodes[nodeid]
        parent.children.append(node)
        
        #print(self.nodes)
            
    def count_boxes(self, box, visited):
        q = deque([box])
        while q: 
            box = q.popleft() 
            if box not in visited:
                #print("visited:",[v.id for v in visited])
                visited.add(box) 
                for child in box.children: 
                    if child not in visited: 
                        q.append(child)

def main():
    n = int(sys.stdin.readline())

    forest = Forest() 
    ints = [int(x) for x in sys.stdin.readline().split()]
    for i in range(len(ints)): 
        forest.add_node(ints[i], i+1)

    q = int(sys.stdin.readline())
    for i in range(q): 
        line = [int(x) for x in sys.stdin.readline().split()]

        visited = set()
        for j in line[1:]: 
            forest.count_boxes(forest.nodes[j], visited)
        print(len(visited))


if __name__=='__main__': 
    main()
