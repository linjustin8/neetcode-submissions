class Solution:
    def check(self, nums: List[int]) -> bool:
        check = 0

        for i in range(len(nums)):
            if nums[i] > nums[(i + 1) % len(nums)]:
                check += 1
                if check > 1:
                    return False
        
        return True