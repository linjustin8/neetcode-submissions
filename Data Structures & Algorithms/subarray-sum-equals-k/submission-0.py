from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixes = defaultdict(int) # prefixVal -> count
        prefixes[0] += 1

        res = prefix = 0
        for n in nums:
            prefix += n
            if prefix - k in prefixes:
                res += prefixes[prefix - k]
            prefixes[prefix] += 1
        
        return res
