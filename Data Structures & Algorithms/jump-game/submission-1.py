class Solution:
    def canJump(self, nums: List[int]) -> bool:
        finish = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= finish:
                finish = i
        
        return finish == 0

            
