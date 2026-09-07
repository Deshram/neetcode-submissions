"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node:
            return 

        queue = deque()
        queue.append(node)

        cl_node = Node()
        cl_node.val = node.val
        clone_queue = deque()
        clone_queue.append(cl_node)

        visited = set()
        while queue:
            og_node = queue.pop()
            clone_node = clone_queue.pop()

            visited.add(og_node.val)

            neighbors = og_node.neighbors
            clone_neighbors = []

            for neighbor in neighbors:
                if neighbor.val in visited: continue
                clone_neighbors.append(neighbor)
                queue.append(neighbor)
                clone_queue.append(neighbor)

            clone_node.neighbors = clone_neighbors

        return cl_node
             