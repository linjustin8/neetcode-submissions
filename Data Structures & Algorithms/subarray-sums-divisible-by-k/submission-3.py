class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        pref = [0] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            pref[i] = pref[i - 1] + nums[i - 1]

        res = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if (pref[j + 1] - pref[i]) % k == 0:
                    res += 1
        
        return res
                