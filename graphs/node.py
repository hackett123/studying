'''
Class represents a node in a graph.

A node has an id and a set of neighbors.

Interface:
    - Can access fields `id` and `neighbors`
    - add_edge(v) -> Put v in u's neighbor's set, or throw an error if already present
    - remove_edge(v) -> Take v out of u's neighbors set, or throw an error if not present
    - cardinality() -> Number of neighbors
    - has_neighbor(v) -> True if there is an edge (u, v)
'''

class Node():

    def __init__(self, id):
        self.neighbors = dict()
        self.id = id

    def get_neighbors(self):
        return self.neighbors.keys()

    
    def add_edge(self, other_node):
        assert(other_node not in self.neighbors)
        self.neighbors[other_node.id] = other_node

    def remove_edge(self, other_node):
        assert(other_node.id in self.neighbors.keys())
        self.neighbors.pop(other_node.id)

    def has_neighbor(self, other_node):
        return other_node.id in self.neighbors.keys()

    def cardinality(self):
        return len(self.neighbors)

    def __str__(self):
        parts = []
        parts.append(f'Node {self.id}.\n')
        if self.neighbors():
            parts.append(f'\tNeighbors: {[neighbor for neighbor in self.out_neighbors.keys()]}')
        return ''.join(parts) + '\n'
