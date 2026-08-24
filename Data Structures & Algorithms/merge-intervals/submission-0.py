class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        start, maxEnd = intervals[0][0], intervals[0][1]
        res = []
        for i in range(len(intervals)):
            if intervals[i][0] <= maxEnd:
                maxEnd = max(maxEnd, intervals[i][1])
            else:
                res.append([start, maxEnd])
                start, maxEnd = intervals[i]
        res.append([start, maxEnd])

        return res