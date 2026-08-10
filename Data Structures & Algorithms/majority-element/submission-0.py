class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        curr = nums[0]
        count = 1
        for n in nums:
            if n != curr:
                count -= 1
                curr = n if count < 0 else curr
                count = max(0, count)
            else:
                count += 1
        
        return curr