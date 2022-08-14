'''
A Directed Graph is defined as G = (V, E) where V is a set of vertices and E is a set of edges.

For each v in V, v is an id for a node object
For each e in E, e = (u, v) and is a link between two node objects where v is in u's neighbor set

Interface:
    - init -> creates empty graph object
    - add_vertex(int u) -> V += (u)
    - add_edge(int u, int v) -> if nodes with id id_one and id_two exist, then E += (u, v)
'''

from node import Node
from graph import Graph

class DirectedGraph(Graph):
    
    def __init__(self):
        self.vertices = {} # map id -> Node object
        self.edges = set() # set of tuples (id_one, id_two)

    def add_vertex(self, id):
        assert (id not in self.vertices.keys())
        self.vertices[id] = Node(id)
    
    def add_vertices(self, *ids):
        for id in ids:
            self.add_vertex(id)

    def add_edge(self, from_id, to_id):
        assert(from_id in self.vertices.keys())
        assert(to_id in self.vertices.keys())
        self.edges.add((from_id, to_id))
        self.vertices[from_id].add_edge(self.vertices[to_id])

    def add_edges(self, *edges):
        for (from_id, to_id) in edges:
            self.add_edge(from_id, to_id)

    def remove_vertex(self, id):
        assert(id in self.vertices.keys())
        '''
        delete node and any edges that have this node
        '''
        self.vertices.pop(id)
        self.edges = ((from_id, to_id) for (from_id, to_id) in self.edges if not (id == from_id or id == to_id))

    def remove_edge(self, from_id, to_id):
        assert((from_id, to_id) in self.edges)
        self.edges.remove((from_id, to_id))

    def has_vertex(self, id):
        return id in self.vertices.keys()

    def has_edge(self, from_id, to_id):
        return (from_id, to_id) in self.edges

    def neighbors(self, id):
        assert(self.has_vertex(id))
        return sorted(self.vertices[id].get_neighbors())

    def cardinality(self):
        return len(vertices)

    def density(self):
        return len(edges)

    def __str__(self):
        sb = []
        sb.append('Vertices:')
        sb.append(f'\t{self.vertices.keys()}')
        sb.append('Edges:')
        sb.append(f'\t{self.edges}')
        return '\n'.join(sb)
