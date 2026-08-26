class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stk = []
        for i in range(len(heights)):
            start = i
            while stk and heights[i] < stk[-1][1]:
                index, height = stk.pop()
                area = (i - index) * height
                res = max(res, area)
                start = index
            stk.append([start, heights[i]])
        
        print()
        while stk:
            index, height = stk.pop()
            area = (len(heights) - index) * height
            res = max(res, area)
    
        return res