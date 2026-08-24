class Solution:
    def solve(self, board: List[List[str]]) -> None:
        dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c):
            if (min(r, c) < 0 or r >= ROWS or c >= COLS
                or board[r][c] == "X" or board[r][c] == "S"):
                return
            
            board[r][c] = "S"
            for newR, newC in dirs:
                dfs(r + newR, c + newC)
        
        for r in range(ROWS):
            dfs(r, 0)
            dfs(r, COLS - 1)
        for c in range(COLS):
            dfs(0, c)
            dfs(ROWS - 1, c)
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "S":
                    board[r][c] = "O"
        