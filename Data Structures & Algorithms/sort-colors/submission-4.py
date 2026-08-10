class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, len(nums) - 1
        while l < r:
            while l < len(nums) and nums[l] == 0:
                l += 1
            if l < len(nums) and nums[r] == 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
            r  -= 1

        r = len(nums) - 1
        while l < r:
            while l < r and nums[l] == 1:
                l += 1
                continue
            if l < len(nums) and nums[r] == 1:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
            r  -= 1

