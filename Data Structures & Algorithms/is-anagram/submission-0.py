class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters_s = [0] * 26
        letters_t = [0] * 26
        for c in s: 
            letters_s[ord(c)-ord("a")]+=1
        for c in t:
            letters_t[ord(c)-ord("a")]+=1
        
        return (letters_s == letters_t)
