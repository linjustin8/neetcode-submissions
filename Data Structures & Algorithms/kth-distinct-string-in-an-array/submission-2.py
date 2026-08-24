from collections import Counter

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        c = Counter(arr)

        for st in arr:
            if c[st] == 1:
                k -= 1
            
            if k == 0:
                return st

        return ""