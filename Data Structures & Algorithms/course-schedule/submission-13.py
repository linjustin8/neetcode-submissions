from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)

        def dfs(course, seen):
            if course in seen:
                return False
            
            if not graph[course]:
                return True
            
            seen.add(course)
            for prereq in graph[course]:
                if not dfs(prereq, seen):
                    return False
            
            seen.remove(course)
            graph[course] = []
            return True
        

        for a, _ in prerequisites:
            if not dfs(a, set()):
                return False
            
        return True
