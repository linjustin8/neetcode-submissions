class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        res = 0
        
        while tickets[k] != 0:
            for t in range(len(tickets)):
                if tickets[t] == 0:
                    continue
                if t == k and tickets[t] == 1:
                    return res + 1

                tickets[t] -= 1
                res += 1

        return 0