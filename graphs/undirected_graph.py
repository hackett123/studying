'''
Class is an abstraction around an undirected graph. In an undirected graph, nodes have neighbors. For an edge (a, b), one may travel from a to b and vice versa.
'''

class UndirectedGraph():

    def __init__(self):
        self.nodes = set()


    def add_nodes(self, *nodes):
        for node in nodes:
            self.add_node(node)
    def add_node(self, node):
        self.nodes.add(node)

    def add_if_missing(self, *nodes):
        for node in nodes:
            if not node in self.nodes:
                self.add_node(node)
    def validate_present(self, *nodes):
        for node in nodes:
            if node not in self.nodes:
                raise Exception("Expected a node to be in the graph which was not found.")

    def add_edge(self, node_one, node_two):
        self.add_if_missing(node_one, node_two)

        # node 1 has to add node 2 to outgoing and incoming
        node_one.add_outgoing_neighbor(node_two)
        node_one.add_incoming_neighbor(node_two)

        # node 2 has to add node 1 to outgoing and incoming
        node_two.add_outgoing_neighbor(node_one)
        node_two.add_incoming_neighbor(node_one)
    
    def trim_edge(self, node_one, node_two):
        self.validate_present(node_one, node_two)
        node_one.remove_edge(node_one, node_two)
        node_two.remove_edge(node_one, node_one)

    def has_edge(self, node_one, node_two):
        if node_one in self.nodes and node_two in self.nodes:
            return node_one.has_outgoing_neighbor(node_two)
        return False
    
    def __str__(self):
        parts = []
        for node in self.nodes:
            parts.append(str(node))
        return ''.join(parts)