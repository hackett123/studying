from directed_graph import DirectedGraph
from bfs import BreadthFirstSearch

import unittest

class TestBfs(unittest.TestCase):
    def testBfsSingleton(self):
        g = DirectedGraph() 
        g.add_vertex(1)
        traversal = BreadthFirstSearch.traverse(g, 1)
        self.assertTrue((0,1) in traversal)
    def testBfsFullGraph(self):
        g = DirectedGraph()
        g.add_vertices(1,2,3,4,5,6,7,8)
        g.add_edges((1,2),(1,3),(1,4),(3,4),(4,5),(7,8))
        traversal = BreadthFirstSearch.traverse(g, 1)
        expected_tuples = [(0, 1), (1, 2), (1, 3), (1, 4), (2, 5)]
        for t in expected_tuples:
            self.assertTrue(t in traversal)

        unreachable_nodes = [7, 8]
        for node in unreachable_nodes:
            self.assertFalse(node in [node_id for (depth, node_id) in traversal])

unittest.main()
