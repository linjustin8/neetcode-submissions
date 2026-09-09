class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])

        res = 0
        curr = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i][0] < curr[1]:
                res += 1
                curr = curr if curr[1] < intervals[i][1] else intervals[i]
                continue
            curr = intervals[i]
        
        return res