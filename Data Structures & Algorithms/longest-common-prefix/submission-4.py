class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pref = strs[0]

        for s in strs:
            if not s:
                return ""
            for i in range(len(s)):
                if i >= len(pref) or s[i] != pref[i]:
                    pref = pref[0:i]
            if len(s) < len(pref):
                pref = pref[:len(s)]
        
        return pref