class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            for s in range(1, i + 1):
                if i - s ** 2 < 0:
                    break
                dp[i] = min(dp[i], 1 + dp[i - s ** 2])
        
        return dp[n]
                