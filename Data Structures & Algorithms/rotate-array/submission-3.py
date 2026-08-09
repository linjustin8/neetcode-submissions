class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.reverse()
        k %= len(nums)
        def reverseInput(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l, r = l + 1, r - 1

        l, r = 0, k - 1
        reverseInput(l, r)
        l, r = k, len(nums) - 1
        reverseInput(l, r)


        

