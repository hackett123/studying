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
'''
from bfs import BreadthFirstSearch


def find_shortest_path(g, u, v):
    bfs_traversal = BreadthFirstSearch.traverse(g, u)
    node_ids = [node for (depth, node, parent) in bfs_traversal]
    contains_target = v in node_ids
    if not contains_target:
        raise Exception(f'Node {v} is not reachable from node {u} in the graph provided.')

    depth = -1
    for (_depth, node, parent) in bfs_traversal:
        if node == v:
            depth = _depth
    path = find_path_back_to_u(bfs_traversal, v, u)
    return (depth, path[::-1])

def find_path_back_to_u(bfs_traversal, v, u):
    '''
    Example of this input could be the graph G=(V,E) where V = {1, 2, 3, 4, 5} and E = {(1, 2), (2, 3), (3, 4), (2, 4)}

    If we consider the bfs traversal for bfs(g, 1, 4), we would get the output:
        [(0, 1, None), (1, 2, 1), (2, 3, 2), (2, 4, 2)]

    If we want to find the path back to u, we would want to see the output as 4 -> 2 -> 1.
    '''
    return recursive_find_path_back_to_u(bfs_traversal, v, u, [])

def recursive_find_path_back_to_u(bfs_traversal, v, u, path):
    '''
        - Base case: v == u -> return v
        - Recursive case: return v + find_path_back_to_u(g, parent, u)
    '''
    if v == u:
        return path + [u]
    
    parent = None
    for (depth, node, _parent) in bfs_traversal:
        if node == v:
            parent = _parent
    
    return recursive_find_path_back_to_u(bfs_traversal, parent, u, path + [v])
    
