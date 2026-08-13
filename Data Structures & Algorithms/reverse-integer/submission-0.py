class Solution:
    def reverse(self, x: int) -> int:
        negative = x < 0
        str_x = str(abs(x))
        str_x = str_x[::-1]
        x = int(str_x)
        x *= -1 if negative else 1

        if not -2**31 < x < 2**31 - 1:
            return 0
        
        return x
        


        