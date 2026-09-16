class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sm = sum(nums)
        if sm % 2:
            return False

        target = sm // 2
        print(target)
        dp = set()

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == target:
                return True
            
            for n in list(dp):
                curr = nums[i] + n
                if curr == target:
                    return True
                dp.add(curr)
            dp.add(nums[i])
        
        return False