class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res, curr = [], []

        def dfs(opens, closes):
            if closes == n:
                res.append("".join(curr))
                return

            if opens == n:
                curr.append(")")
                dfs(opens, closes + 1)
                curr.pop()
                return
            
            curr.append("(")
            dfs(opens + 1, closes)
            curr.pop()
            if curr and closes < opens:
                curr.append(")")
                dfs(opens, closes + 1)
                curr.pop()
        
        dfs(0, 0)
        return res