"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        cloneMap = {} # oldNode -> newNode

        def dfs(node, cloneMap): # return newNode to map to
            if node in cloneMap:
                return cloneMap[node]
            
            copy = Node(node.val)
            cloneMap[node] = copy
            for n in node.neighbors:
                copy.neighbors.append(dfs(n, cloneMap))
            return copy
        
        return dfs(node, cloneMap)


            
