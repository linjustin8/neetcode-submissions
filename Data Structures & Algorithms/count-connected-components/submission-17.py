from collections import defaultdict

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        s = set(range(n))
        q = deque()
        res = 0
        
        for i in range(n):
            if i not in s:
                continue
            
            res += 1
            q.append(i)
            while q:
                curr = q.popleft()
                print(curr)
                if curr in s:
                    s.remove(curr)
                for neigh in adj[curr]:
                    if neigh not in s:
                        continue
                    q.append(neigh)
        
        return res
