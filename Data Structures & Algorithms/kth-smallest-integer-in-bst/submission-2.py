# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nodes = []

        def dfs(node):
            nonlocal nodes
            if not node or len(nodes) == k:
                return
            
            dfs(node.left)
            if len(nodes) < k:
                nodes.append(node)
            dfs(node.right)
            return
        
        dfs(root)
        print([node.val for node in nodes])
        return nodes[-1].val
