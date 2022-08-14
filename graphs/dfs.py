class DepthFirstSearch:

    @staticmethod
    def traverse(g, starting_node):
        '''
        Delegates computation to helper method.
        Returns a list of nodes in the order we visited them
        '''
        return DepthFirstSearch._traverse(g, starting_node, [starting_node], 1)

    @staticmethod
    def _traverse(g, u, visited, depth):
        '''
        Recursive helper. Iterates over a node's neighbors and recursively visits each one, if we haven't
        visited it yet. Returns ordered list of the nodes we saw.
        '''
        for v in g.neighbors(u):
            if v not in visited:
                visited.append(v)
                DepthFirstSearch._traverse(g, v, visited, depth + 1)
        return visited
