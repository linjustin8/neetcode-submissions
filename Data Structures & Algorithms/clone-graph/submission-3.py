"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        copies = {}


        def clone(node):
            if node in copies:
                return copies[node]
            
            if not node:
                return None
            
            newNode = Node(node.val)
            copies[node] = newNode 
            for n in node.neighbors:
                newNode.neighbors.append(clone(n))

            return newNode

        return clone(node)           