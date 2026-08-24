class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        s = set()
        res = []
        for r in grid:
            for c in r:
                if c not in s:
                    s.add(c)
                else:
                    res.append(c)
                    
        
        for i in range(1, len(s) + 2):
            if i not in s:
                res.append(i)
        
        return res
                