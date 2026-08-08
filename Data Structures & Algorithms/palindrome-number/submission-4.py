class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
            
        n = list(str(x))
        rev = n.copy()
        rev.reverse()

        return n == rev