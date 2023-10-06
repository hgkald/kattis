import sys 
import queue
import random 
from functools import total_ordering 

class Graph:
    def __init__(self):
        self.nodes = {}
        self.edges = []

    def node(self, val):
        return self.nodes[int(val)]

    def add_node(self, node):
        self.nodes[node.val] = node

    def add_edge(self, edge):
        self.edges.append(edge)

class Node:
    def __init__(self, val):
        self.val = int(val)
        self.edges = []

    def add_edge(self, edge):
        self.edges.append(edge)


class Edge:
    def __init__(self, n1, n2, w):
        self.node1 = n1
        self.node2 = n2
        self.weight = int(w)

    def other_node(self, node):
        if node is self.node1:
            return self.node2
        elif node is self.node2:
            return self.node1
        else:
            return None

@total_ordering
class ComparableItem: 
    def __init__(self, priority, item): 
        self.item = item 
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority

    def __gt__(self, other):
        return self.priority > other.priority

    def __eq__(self, other):
        return self.priority == other.priority


def prim(g): 
    q = queue.PriorityQueue()
    parents = {}
    cost = 0

    some_node = random.choice(list(g.nodes.values()))
    q.put(ComparableItem(0, (None, some_node)))

    while not q.empty(): 
        (parent, node) = q.get().item
        if node not in parents: 
            parents[node] = parent
            for edge in node.edges: 
                child = edge.other_node(node)
                #q.put(ComparableItem(edge.weight, (node, child)))
                q.put(ComparableItem(edge.weight, (node, child)))
                cost += edge.weight

    return (cost, parents)

def __main__(): 
    vals = input().split()
    while vals != ['0','0']: 
        g = Graph()
        for i in range(int(vals[1])): 
            [n1, n2, w] = [int(val) for val in input().split()]
            if n1 not in g.nodes.keys(): 
                node1 = Node(n1)
                g.add_node(node1)
            else: 
                node1 = g.nodes[n1]

            if n2 not in g.nodes.keys(): 
                node2 = Node(n2)
                g.add_node(node2)
            else: 
                node2 = g.nodes[n2]

            edge = Edge(node1, node2, w)
            g.add_edge(edge)
            node1.add_edge(edge)
            node2.add_edge(edge)

        if len(g.edges) > 0: 
            cost, parents = prim(g)
            print(cost)
            
            for node in parents: 
                if parents[node]:
                    child = parents[node]
                    print(node.val, child.val)
            
        else: 
            print("Impossible")
        vals = input().split()


__main__()


