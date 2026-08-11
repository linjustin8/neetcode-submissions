class StockSpanner:

    def __init__(self):
        self.stk = [] # [price, span]

    def next(self, price: int) -> int:
        currStock = [price, 1]
        while self.stk and self.stk[-1][0] <= price:
            currStock[1] += self.stk[-1][1]
            self.stk.pop()
        self.stk.append(currStock)
        return currStock[1]
 

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)