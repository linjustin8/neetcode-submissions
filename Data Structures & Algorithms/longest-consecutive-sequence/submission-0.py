class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        s = set(nums)

        for n in nums:
            if n - 1 not in s:
                length = 1
                while (n + length) in s:
                    length += 1
                res = max(res, length)
        
        return res