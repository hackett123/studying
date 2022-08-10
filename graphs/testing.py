from node import Node
from undirected_graph import UndirectedGraph

class Testing:

    def make_basic_graph(self):
        node_one = Node(1)
        node_two = Node(2)
        node_three = Node(3)
        g = UndirectedGraph()
        g.add_nodes(node_one, node_two, node_three)
        g.add_edge(node_one, node_two)
        g.add_edge(node_two, node_three)
        return g

t = Testing()
g = t.make_basic_graph()
print(str(g))
