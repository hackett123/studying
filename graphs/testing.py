from node import Node
from undirected_graph import UndirectedGraph

class Testing:
    def test_make_graph(self):
        node_one = Node(1)
        node_two = Node(2)
        node_three = Node(3)
        g = UndirectedGraph()
        g.add_nodes(node_one, node_two, node_three)
        g.add_edge(node_one, node_two)
        g.add_edge(node_two, node_three)
        print(g)

t = Testing()
t.test_make_graph()