'''
Class implements the shortest path problem for unweighted graphs.

The algorithm is as follows:

- Problem Description: Given input G=(V,E) with a source node u and a target node v, find the shortest path from u to v.

- Algorithm:
    - bfs(g, u)
    - If output contains v, then there exists a path
    - The length of the path is the depth to v.

- Proof:
    - Assume for sake of contradiction that there exists a shorter path (u, ..., v) in G.
    - bfs proceeds in a "search party" fashion, expanding out in a ring, going one step deeper each iteration
    - If there exists a shorter path (u, ..., v) in G, then the search would have discovered v earlier.

Our output returns the length only.

One can imagine an implementation which also returns the path (u, ..., v). We will do that separately. But to do so, we would make the
following modifications to our algorithm for bfs:
    - bfs currently returns a list of tuples (depth, node). There is no way to tell what parent a node was recursed into from. In order
    to also return paths themselves, we need to have the tuple expanded to (depth, node, parent). Then, given a bfs output [(depth1, node1, parent1),
    (depth2, node2, parent2), ...] we can recursively find the parent of v until we encounter u.
'''
from bfs import BreadthFirstSearch

class ShortestPath():

    @staticmethod
    def find_shortest_path(g, u, v):
        bfs_traversal = BreadthFirstSearch.traverse(g, u)
        node_ids = [node for (depth, node) in bfs_traversal]
        contains_target = v in node_ids
        if not contains_target:
            raise Exception(f'Node {v} is not reachable from node {u} in the graph provided.')
        for (depth, node) in bfs_traversal:
            if node == v:
                return depth
            
