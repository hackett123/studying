import unittest
from node import Node

class TestConstructor(unittest.TestCase):
    def runTest(self):
        node = Node(1)
        self.assertEqual(1, node.id)
        self.assertEqual({}, node.neighbors)

class TestAddEdge(unittest.TestCase):
    def testSingleAdd(self):
        node = Node(1)
        node2 = Node(2)
        node.add_edge(node2)
        self.assertEqual({2:node2}, node.neighbors)
    def testMultipleAdd(self):
        node = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node.add_edge(node2)
        node.add_edge(node3)
        self.assertEqual({2:node2,3:node3}, node.neighbors)

class TestRemoveEdge(unittest.TestCase):
    def testRemoveOnlyEdge(self):
        node, node2 = Node(1), Node(2)
        node.add_edge(node2)
        node.remove_edge(node2)
        self.assertEqual({}, node.neighbors)
    
    def testRemoveOneOfMultipleEdges(self):
        node, node2, node3 = Node(1), Node(2), Node(3)
        node.add_edge(node2)
        node.add_edge(node3)
        node.remove_edge(node2)
        self.assertEqual({3:node3}, node.neighbors)

class TestHasNeighbor(unittest.TestCase):
    def testFalse(self):
        node = Node(1)
        self.assertFalse(node.has_neighbor(Node(7)))

    def testTrue(self):
        node = Node(1)
        node2 = Node(2)
        node.add_edge(node2)
        self.assertTrue(node.has_neighbor(node2))

class TestCardinality(unittest.TestCase):
    def testEmpty(self):
        self.assertEquals(0, Node(5).cardinality())
    def testNonEmpty(self):
        node, node2 = Node(5), Node(10)
        node.add_edge(node2)
        self.assertEquals(1, node.cardinality())
        self.assertEquals(0, node2.cardinality())

unittest.main()
