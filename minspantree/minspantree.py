import sys 
import random 
from functools import total_ordering 
import heapq
#import cProfile 

class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = {}

    def node(self, val):
        return self.nodes[int(val)]

    def add_node(self, node):
        self.nodes[node.val] = node

    def add_edge(self, edge):
        key = frozenset((edge.node1.val, edge.node2.val))
        self.edges[key] = edge

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

class MyQueue:
    def __init__(self):
        self.items = []

    def empty(self):
        return len(self.items) == 0

    def get(self):
        rv = heapq.heappop(self.items)
        return rv
    
    def put(self, item):
        heapq.heappush(self.items, item)


def prim(g): 
    q = MyQueue()
    parents = {}

    some_node = random.choice(g.nodes)
    q.put((0, None, some_node.val))

    while not q.empty(): 
        (weight, parentid, nodeid) = q.get()
        parent = None 
        if parentid: 
            parent = g.nodes[parentid]
        node = g.nodes[nodeid]
        if node not in parents:
            parents[node] = parent
            for edge in node.edges: 
                child = edge.other_node(node)
                if child not in parents: 
                    q.put((edge.weight, node.val, child.val))

    return parents

def __main__(): 
    vals = input().split()
    while vals != ['0','0']:
        g = Graph()
        n = int(vals[0])
        m = int(vals[1])
        g.nodes = [None] * n

        for i in range(int(vals[1])): 
            [n1, n2, w] = [int(val) for val in input().split()]
            if not g.nodes[n1]: 
                node1 = Node(n1)
                g.nodes[n1] = node1
            else: 
                node1 = g.nodes[n1]

            if not g.nodes[n2]: 
                node2 = Node(n2)
                g.nodes[n2] = node2
            else: 
                node2 = g.nodes[n2]

            edge = Edge(node1, node2, w)
            g.add_edge(edge)
            node1.add_edge(edge)
            node2.add_edge(edge)

        if len(g.edges) > 0: 
            parents = prim(g)
            nodes_reached = len(parents)
            if nodes_reached < n: 
                print("Impossible")
                continue

            edges = [] 
            cost = 0
            for node in parents: 
                if parents[node]:
                    parent = parents[node]
                    cost += g.edges[frozenset((parent.val, node.val))].weight
                    edge = [parent.val, node.val]
                    edge.sort()
                    edges.append(edge)
            print(cost)

            edges.sort()
            for e in edges: 
                print(e[0], e[1])
        else: 
            print("Impossible")
        vals = input().split()


#cProfile.run('__main__()')
__main__()


