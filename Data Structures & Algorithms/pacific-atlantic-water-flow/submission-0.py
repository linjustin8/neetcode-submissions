from collections import defaultdict

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = []
        atlantic = []

        for i in range(len(heights)):
            pacific.append([i, 0])
        for j in range(len(heights[0])):
            pacific.append([0, j])
        for i in range(len(heights)):
            atlantic.append([i, len(heights[0]) - 1])
        for j in range(len(heights[0])):
            atlantic.append([len(heights) - 1, j])
        
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
        def dfs(r, c, prev, seen):
            if (r < 0 or r >= len(heights) or c < 0 or c >= len(heights[0])
             or (r, c) in seen or heights[r][c] < prev):
                return
            seen.add((r, c))

            for row, col in dirs:
                dfs(row + r, col + c, heights[r][c], seen)
        
        pacific_set = set()
        for r, c in pacific:
            dfs(r, c, heights[r][c], pacific_set)
        atlantic_set = set()
        for r, c in atlantic:
            dfs(r, c, heights[r][c], atlantic_set)
            
        res = []
        for r, c in pacific_set:
            if (r, c) in atlantic_set:
                res.append([r, c])
        
        return res
