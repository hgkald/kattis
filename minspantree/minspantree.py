import sys 
import queue
import random 
from functools import total_ordering 
from collections import defaultdict 
import heapq
#import cProfile 

class Graph:
    def __init__(self):
        self.nodes = {}
        self.edges = defaultdict(list)
        self.num_edges = 0

    def node(self, val):
        return self.nodes[int(val)]

    def add_node(self, node):
        self.nodes[node.val] = node

    def add_edge(self, edge):
        key = frozenset((edge.node1.val, edge.node2.val))
        self.edges[key].append(edge)
        self.num_edges += 1

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
    #q = queue.PriorityQueue()
    q = MyQueue()
    parents = {}

    some_node = random.choice(list(g.nodes.values()))
    q.put(ComparableItem(0, (None, some_node)))

    while not q.empty(): 
        (parent, node) = q.get().item
        if node not in parents:
            parents[node] = parent
            for edge in node.edges: 
                child = edge.other_node(node)
                #if child not in parents: 
                q.put(ComparableItem(edge.weight, (node, child)))

    return parents

def __main__(): 
    vals = input().split()
    while vals != ['0','0']:
        g = Graph()
        n = int(vals[0])
        m = int(vals[1])
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

        if g.num_edges > 0: 
            parents = prim(g)
            nodes_reached = len(parents)
            if nodes_reached < n: 
                print("Impossible")
            else: 
                edges = [] 
                cost = 0
                for node in parents: 
                    if parents[node]:
                        parent = parents[node]
                        weights = [e.weight for e in g.edges[frozenset((parent.val, node.val))]]
                        edge = [parent.val, node.val]
                        cost += min(weights)
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


