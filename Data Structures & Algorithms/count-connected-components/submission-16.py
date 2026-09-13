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
            print(s)
            if i not in s:
                continue
            
            res += 1
            q.append((i, -1))
            while q:
                curr, parent = q.popleft()
                if curr in s:
                    s.remove(curr)
                for neigh in adj[curr]:
                    if neigh not in s or neigh == parent:
                        continue
                    q.append((neigh, curr))
        
        return res
