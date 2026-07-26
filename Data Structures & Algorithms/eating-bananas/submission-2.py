class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        while l < r:
            m = l + (r - l) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(float(p)/float(m))
            if hours <= h:
                r = m  
            else:
                l = m + 1
        return l
