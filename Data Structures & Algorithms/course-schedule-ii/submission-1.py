from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = defaultdict(list)
        for crs, pre in prerequisites:
            prereq[crs].append(pre)

        res = []
        cycle, checked = set(), set()
        def dfs(c):
            if c in cycle:
                return False
            if c in checked:
                return True
            
            cycle.add(c)
            for p in prereq[c]:
                if not dfs(p):
                    return False
            
            cycle.remove(c)
            checked.add(c)
            res.append(c)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return []
        
        return res

