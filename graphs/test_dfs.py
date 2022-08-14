from directed_graph import DirectedGraph
from dfs import DepthFirstSearch

import unittest

class TestDfs(unittest.TestCase):
    def testDfsSingleton(self):
        g = DirectedGraph()
        g.add_vertex(1)
        traversal = DepthFirstSearch.traverse(g, 1)
        self.assertEqual([1], traversal)
    def testDfsLinkedList(self):
        g = DirectedGraph()
        g.add_vertices(1, 2, 3, 4, 5)
        g.add_edges((1,2),(2,3),(3,4),(4,5))
        traversal = DepthFirstSearch.traverse(g, 1)
        self.assertEqual([1,2,3,4,5], traversal)

        traversal_from_sink = DepthFirstSearch.traverse(g, 5)
        self.assertEqual([5], traversal_from_sink)

    def testDfsBranches(self):
        g = DirectedGraph()
        g.add_vertices(1,2,3,4,5)
        g.add_edges((1,5), (5,4), (4,3), (3,2), (1,2))
        # g sorts the neighbors so we should visit 2 before 5 so we should get 1 2 5 4 3
        traversal = DepthFirstSearch.traverse(g, 1)
        self.assertEqual([1,2,5,4,3], traversal)

    def testDfsCycles(self):
        g = DirectedGraph()
        g.add_vertices(1,2,3,4)
        g.add_edges((1,2),(2,3),(3,4),(4,1))
        traversal = DepthFirstSearch.traverse(g,1)
        self.assertEqual([1,2,3,4], traversal)

        traversal_from_other_node = DepthFirstSearch.traverse(g, 3)
        self.assertEqual([3,4,1,2], traversal_from_other_node)

unittest.main()
