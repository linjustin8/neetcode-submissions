# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0

        def dfs(root, goodVal):
            nonlocal res
            if not root:
                return 
            
            res += 1 if root.val >= goodVal else 0
            goodVal = max(goodVal, root.val)
            dfs(root.left, goodVal)
            dfs(root.right, goodVal)
        
        if not root:
            return 0

        dfs(root, root.val)
        return res