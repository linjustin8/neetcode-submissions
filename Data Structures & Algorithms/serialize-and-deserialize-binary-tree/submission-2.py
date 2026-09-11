# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        def dfs(node):
            if not node:
                res.append("n")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ".".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        
        parsed = data.split(".")

        def dfs(i):
            if i == len(parsed) or parsed[i] == "n":
                return None, i + 1

            root = TreeNode(int(parsed[i]))
            root.left, nextIdx = dfs(i + 1)
            root.right, nextIdx = dfs(nextIdx)

            return root, nextIdx

        root, _ = dfs(0)
        return root