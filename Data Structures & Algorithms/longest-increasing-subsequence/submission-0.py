class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = {}
        cache[len(nums)] = 0

        def dfs(i):
            if i in cache:
                return cache[i]
            inc = 1
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    inc = max(inc, 1 + dfs(j))
            cache[i] = inc
            return inc
        
        for i in range(len(nums)):
            dfs(i)
        return max(cache.values())
            