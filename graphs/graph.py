'''
A Graph G = (V, E) consists of a set of vertices V and a set of edges E.

This interface consists of the following methods:
    - add_vertex(id)
    - add_vertices(*ids)
    - add_edge(from, to)
    - add_edges(*edges)
    - remove_vertex(id)
    - remove_edge(from, to)
    - has_vertex(id)
    - has_edge(from, to)
    - neighbors(id)
    - cardinality() -> # of vertices
    - density() -> # of edges
'''

class Graph:

    def add_vertex(self, id):
        raise NotImplementedError("Missing implementation!")

    def add_vertices(self, *ids):
        raise NotImplementedError("Missing implementation!")

    def add_edge(self, from_id, to_id):
        raise NotImplementedError("Missing implementation!")

    def add_edges(self, *edges):
        raise NotImplementedError("Missing implementation!")

    def remove_vertex(self, id):
        raise NotImplementedError("Missing implementation!")

    def remove_edge(self, from_id, to_id):
        raise NotImplementedError("Missing implementation!")

    def has_vertex(self, id):
        raise NotImplementedError("Missing implementation!")

    def has_edge(self, from_id, to_id):
        raise NotImplementedError("Missing implementation!")

    def neighbors(self, id):
        raise NotImplementedError("Missing implementation!")

    def cardinality(self):
        raise NotImplementedError("Missing implementation!")

    def density(self):
        raise NotImplementedError("Missing implementation!")
        
