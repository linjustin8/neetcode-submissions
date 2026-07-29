class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0 for i in range(len(s))]
        dp[0] = 1 if s[0] != "0" else 0

        for i in range(1, len(s)):
            if s[i] != "0":
                dp[i] += dp[i - 1]

            two_digit = int(s[i - 1:i + 1])

            if 10 <= two_digit <= 26:
                dp[i] += dp[i - 2] if i >= 2 else 1
        
        return dp[-1]
            