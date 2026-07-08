class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        seen = set()

        def dfs(r, c, seen):
            
            if (r < 0 or c < 0 or r >= ROW or c >= COL
                or (r, c) in seen or grid[r][c] == 1):
                return 0
            
            if r == ROW - 1 and c == COL - 1:
                return 1
            
            seen.add((r, c))
            
            count = 0
            for x, y in dirs:
                count += dfs(r+x, c+y, seen)
            seen.remove((r,c))

            return count
        
        return dfs(0, 0, seen)
            
