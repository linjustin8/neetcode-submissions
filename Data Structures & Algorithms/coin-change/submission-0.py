class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [math.inf] * (amount + 1)
        dp[0] = 0
 
        for amt in range(1, amount + 1):
            for coin in coins:
                remain = amt - coin
                if remain < 0:
                    continue
                dp[amt] = min(dp[amt], 1 + dp[remain])
        
        return dp[amount] if dp[amount] != math.inf else -1