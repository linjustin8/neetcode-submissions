# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        currMax = -math.inf
        def dfs(node):
            nonlocal currMax
            if not node:
                return 0
            
            currMax = max(currMax, node.val)
            left = dfs(node.left)
            right= dfs(node.right)
            curr = node.val + left + right
            currMax = max(
                currMax,
                curr,
                node.val + left, 
                node.val + right
            )

            currPath = node.val + max(left, right)
            
            return 0 if currPath < 0 else currPath

        dfs(root)
        return currMax
            