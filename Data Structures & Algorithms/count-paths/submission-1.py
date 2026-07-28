class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0 for i in range(n)] for j in range(m)]

        for i in range(m):
            grid[i][0] = 1
        for j in range(n):
            grid[0][j] = 1
        
        for r in range(1, m):
            for c in range(1, n):
                grid[r][c] = grid[r-1][c] + grid[r][c-1]
        
        return grid[-1][-1]