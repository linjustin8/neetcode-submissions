from collections import Counter
import heapq

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        c = Counter(hand)
        c = list(c.items())
        heapq.heapify(c)
        for _ in range(len(hand)//groupSize):
            curr = []
            for _ in range(groupSize):
                if not c:
                    return False
                card, count = heapq.heappop(c)
                if curr and card != curr[-1][0] + 1:
                    return False
                curr.append((card, count - 1))
            for card in curr:
                if card[1] > 0:
                    heapq.heappush(c, card)


        return True