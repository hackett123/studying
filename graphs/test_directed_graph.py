import unittest
from directed_graph import DirectedGraph

class TestConstructor(unittest.TestCase):
    def runTest(self):
        g = DirectedGraph()
        self.assertEqual({}, g.vertices)
        self.assertEqual(set(), g.edges)

class TestRemoveNodes(unittest.TestCase):
    def runTest(self):
        g = DirectedGraph()
        g.add_vertices(1, 2, 3, 4)
        g.add_edges((1, 2), (1, 3), (1, 4))
        g.remove_vertex(4)
        self.assertEqual(set([1, 2, 3]), g.vertices.keys())
        self.assertEqual(set([(1, 2), (1, 3)]), set(g.edges))
        g.remove_vertex(1)
        self.assertEqual([2, 3], list(g.vertices.keys()))
        self.assertEqual(set(), set(g.edges))

class TestRemoveEdge(unittest.TestCase):
    def runTest(self):
        g = DirectedGraph()
        g.add_vertices(1, 2, 3)
        g.add_edges((1, 2), (2, 3), (1, 3))
        g.remove_edge(1, 3)
        self.assertEqual([1,2,3], list(g.vertices.keys()))
        self.assertEqual(set([(1, 2), (2, 3)]), set(g.edges))

unittest.main()
