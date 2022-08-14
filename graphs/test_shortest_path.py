from shortest_path import ShortestPath
from directed_graph import DirectedGraph
import unittest

class TestShortestPath(unittest.TestCase):
    def testShortestPathDNE(self):
        g = DirectedGraph()
        g.add_vertices(1, 2, 3)
        g.add_edge(1, 2)
        self.assertRaises(Exception, ShortestPath.find_shortest_path, g, 1, 3)

    def testShortestPathDistanceOne(self):
        g = DirectedGraph()
        g.add_vertices(1,2,3,4,5)
        g.add_edges((1,2),(2,3),(4,5))
        distance = ShortestPath.find_shortest_path(g, 2, 3)
        self.assertEqual(1, distance)

    def testShortestPathDistanceMoreThanOne(self):
        g = DirectedGraph()
        g.add_vertices(1,2,3,4,5)
        g.add_edges((1,2),(2,3),(1,4),(3,4))
        self.assertEqual(1, ShortestPath.find_shortest_path(g, 1, 4))
        self.assertEqual(2, ShortestPath.find_shortest_path(g, 2, 4))

unittest.main()
