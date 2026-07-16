class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) < 3:
            return min(cost)
        cost.append(0)

        dp1, dp2 = cost[-2], cost[-1]
        for i in range(len(cost) - 1, -1 , -1):
            dp = min(cost[i] + dp1, cost[i] + dp2)
            dp1, dp2, = dp2, dp
        
        return min(dp1, dp2)