from directed_graph import DirectedGraph
import shortest_path

import unittest

class TestFindPathBackToU(unittest.TestCase):
    '''
     graph G=(V,E) where V = {1, 2, 3, 4, 5} and E = {(1, 2), (2, 3), (3, 4), (2, 4)}
     For bfs(g, 1, 4), we would get the output:
        [(0, 1, None), (1, 2, 1), (2, 3, 2), (2, 4, 2)]
    '''
    
    def testPathBack(self):
        self.assertEqual([4, 2, 1], shortest_path.find_path_back_to_u([(0, 1, None), (1, 2, 1), (2, 3, 2), (2, 4, 2)], 4, 1))

class TestShortestPath(unittest.TestCase):
    def testshortest_pathDNE(self):
        g = DirectedGraph()
        g.add_vertices(1, 2, 3)
        g.add_edge(1, 2)
        self.assertRaises(Exception, shortest_path.find_shortest_path, g, 1, 3)

    def testshortest_pathDistanceOne(self):
        g = DirectedGraph()
        g.add_vertices(1,2,3,4,5)
        g.add_edges((1,2),(2,3),(4,5))
        distance = shortest_path.find_shortest_path(g, 2, 3)
        self.assertEqual((1, [2, 3]), distance)

    def testshortest_pathDistanceMoreThanOne(self):
        g = DirectedGraph()
        g.add_vertices(1,2,3,4,5)
        g.add_edges((1,2),(2,3),(1,4),(3,4))
        self.assertEqual((1, [1, 4]), shortest_path.find_shortest_path(g, 1, 4))
        self.assertEqual((2, [2, 3, 4]), shortest_path.find_shortest_path(g, 2, 4))

unittest.main()
