from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        c = Counter(t)

        if len(s) < len(t):
            return ""
        
        l = 0
        valid = 0
        chars = defaultdict(int)
        for r in range(len(s)):
            if c[s[r]] > 0:
                valid += 1 if chars[s[r]] < c[s[r]] else 0
                chars[s[r]] += 1

            while valid == len(t):
                res = s[l:r + 1] if r - l + 1 < len(res) or res == "" else res
                chars[s[l]] -= 1 if c[s[l]] > 0 else 0
                valid -= 1 if chars[s[l]] < c[s[l]] else  0
                l += 1
            
        return res