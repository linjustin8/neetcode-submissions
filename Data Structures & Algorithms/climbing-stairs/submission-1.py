class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        
        dp1, dp2 = 1, 2
        for i in range(2, n):
            dp = dp1 + dp2
            dp1, dp2 = dp2, dp
        
        return dp2