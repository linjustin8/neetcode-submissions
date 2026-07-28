class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))

        def dfs(row, col):
            if (not 0 <= row < rows or not 0 <= col < cols or
                board[row][col] != "O" ):
                return
            
            board[row][col] = "S"
            for r, c in dirs:
                dfs(row + r, col + c)
        
        for row in range(rows):
            dfs(row, 0)
            dfs(row, cols - 1)
        for col in range(cols):
            dfs(0, col)
            dfs(rows - 1, col)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "S":
                    board[r][c] = "O"
