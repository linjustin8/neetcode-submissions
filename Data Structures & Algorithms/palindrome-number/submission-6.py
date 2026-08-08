class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
            
        n = list(str(x))

        l, r = 0, len(n) - 1
        while l < r:
            if n[l] != n[r]:
                return False
            l += 1
            r -= 1
        
        return True
        