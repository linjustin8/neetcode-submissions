class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = l = 0
        for r in range(len(prices)):
            while l < r and prices[l] > prices[r]:
                l += 1
            res = max(res, prices[r] - prices[l])

        return res