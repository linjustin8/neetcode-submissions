class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        self.maxNums = maxNumbers
        self.filled = 0
        self.slots = [True for n in range(self.maxNums)]


    def get(self) -> int:
        if self.filled == self.maxNums:
            return -1
        for i in range(len(self.slots)):
            if self.slots[i]:
                self.slots[i] = False
                self.filled += 1
                return i

    def check(self, number: int) -> bool:
        return self.slots[number]

    def release(self, number: int) -> None:
        if not self.slots[number]:
            self.filled -= 1
        self.slots[number] = True


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)