'''
BFS, or Breadth First Search, is a fundamental graph traverse algorithm. The algorithm is as follows:
- Given a starting node u in a graph G=(V,E):
- Visit all the neighbors of u, and then for each neighbor, bfs the neighbor
- Finally, return the visited list.


Our implementation reads a bit complicated because we track a depth field as well and put the output
list as a tuple of (depth, node) instead of just a list of nodes. We do this on purpose to solve the
shortest path problem, whwch we will do next.
'''

from graph import Graph

class BreadthFirstSearch():

    @staticmethod
    def traverse(g, starting_node):
        '''
        Delegate computation to recursive helper
        '''
        visited = [(0, starting_node)]
        return BreadthFirstSearch._traverse(g, starting_node, visited, 1)

    @staticmethod
    def _traverse(g, u, visited, depth):
        '''
        Base Case: u has no neighbors or we have visited all the neighbors
        Recursive Definition: bfs on the neighbors after visiting each neighbor
        Return: Visited list

        Note: to make the recursion eaier to understand, you can imagine a different implementation
        where we add a statement before `for v in to_visit` to say `if len(to_visit) == 0: return visited`
        as it would do the same thing
        '''
        to_visit = []
        for neighbor in g.neighbors(u):
            if neighbor not in [node_id for (depth, node_id) in visited]:
                visited.append((depth, neighbor))
                to_visit.append(neighbor)
        for v in to_visit:
            BreadthFirstSearch._traverse(g, v, visited, depth + 1)
        return visited

