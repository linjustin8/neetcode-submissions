from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)

        for a, b in prerequisites:
            adj[a].append(b)
        
        def dfs(course, visit):
            if course in visit:
                return False
            
            if not adj[course]:
                return True
            
            visit.add(course)
            for c in adj[course]:
                if not dfs(c, visit):
                    return False
            
            visit.remove(course)
            adj[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course, set()):
                return False
        
        return True