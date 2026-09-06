from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        mp = defaultdict(dict)
        for a, b, t in times:
            mp[a][b] = t
        
        heap = []
        bestTime = {}
        heap.append((0, k))
        bestTime[k] = 0
        
        while heap:
            time, node = heapq.heappop(heap)
            for neighbor, t in mp[node].items():
                currTime = t + time
                if currTime < bestTime.get(neighbor, math.inf):
                    bestTime[neighbor] = currTime
                    heapq.heappush(heap, (currTime, neighbor))
        
        totalTime = 0
        for _, time in bestTime.items():
            totalTime = max(time, totalTime)
            
        return totalTime if len(bestTime) == n else -1