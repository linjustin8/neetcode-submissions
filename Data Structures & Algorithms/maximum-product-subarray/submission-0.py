class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMin, curMax = 1, 1

        for n in nums:
            if n == 0:
                curMin = curMax = 1
                continue

            temp = n * curMin
            curMin, curMax = min(n, n * curMax, n * curMin), max(n, n * curMax, temp)
            res = max(res, curMax)
        
        return res