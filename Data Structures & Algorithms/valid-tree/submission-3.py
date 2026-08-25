from collections import defaultdict, deque

class Solution:
    def validTree(self, count: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        seen = set()
        q = deque()
        q.append([0, -1])

        while q:
            node, parent = q.popleft()
            if node in seen:
                return False
            seen.add(node)
            for n in adj[node]:
                if n != parent:
                    q.append([n, node])
            
        
        return len(seen) == count