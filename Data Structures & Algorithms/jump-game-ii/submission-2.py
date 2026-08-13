from collections import deque

class Solution:
    def jump(self, nums: List[int]) -> int:
        currMax = 0
        res = 0
        q = deque([0]) # indices within nums

        while q:
            if currMax >= len(nums) - 1:
                return res

            currMax = q[0] + nums[q[0]]
            res += 1
            levels = len(q)
            for i in range(len(q)):
                index = q.popleft()
                currMax = max(currMax, index + nums[index])
                if i == levels - 1:
                    for j in range(index + 1, min(currMax + 1, len(nums))):
                        if j == len(nums):
                            return res
                        q.append(j)

        return res

