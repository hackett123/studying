'''
Class represents a node in a graph.

A node consists of a set of pointers to incoming nodes and outgoing nodes.

Incoming nodes are tracked for undirected graphs and for convenience for directed graphs.

In directed graph, a -> b does not mean b -> a. In a undirected graph, if a -> b then b -> a.
    In other words, in directed graphs, if a is in b's incoming list, means b is in a's outgoing list, but it does not mean thata is in b's outgoing list.

Interface:
    - neighbors() -> returns list of outgoing neighbors. That is, for some graph G, given
        an edge (u, v), u.neighbors() must contain v.
    - remove_edge() -> If u contains an outgoing neighbor to v, we remove it.
'''

class Node():

    def __init__(self, id):
        self.in_neighbors = set()
        self.out_neighbors = set()
        self.id = id

    def neighbors(self):
        return self.out_neighbors

    def remove_edge(self, from_node, to_node):
        if self == from_node:
            # we are removing from outgoing
            self.out_neighbors.remove(to_node)
        elif self == to_node:
            self.in_neighbors.remove(to_node)
        else:
            raise Exception("Expected self to be one of the nodes while executing remove_edge")
    
    def add_outgoing_neighbor(self, new_node):
        self.out_neighbors.add(new_node)
    
    def add_incoming_neighbor(self, new_node):
        self.in_neighbors.add(new_node)

    def has_incoming_neighbor(self, other_node):
        return other_node in self.in_neighbors

    def has_outgoing_neighbor(self, other_node):
        return other_node in self.out_neighbors

    def __str__(self):
        parts = []
        parts.append(f'Node {self.id}.\n')
        if self.neighbors():
            parts.append(f'\tIncoming Neighbors: {[neighbor.id for neighbor in self.in_neighbors]}')
            parts.append('\n')
            parts.append(f'\tOutgoing Neighbors: {[neighbor.id for neighbor in self.out_neighbors]}')
        return ''.join(parts) + '\n'
