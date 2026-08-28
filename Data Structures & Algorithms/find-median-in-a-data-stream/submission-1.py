class MedianFinder:

    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        self.nums.append(num)
        self.nums.sort()

    def findMedian(self) -> float:
        mid = len(self.nums) // 2
        if len(self.nums) % 2 == 0:
            mid2 = mid - 1 
            return (self.nums[mid] + self.nums[mid2]) / 2.0
        else:
            return self.nums[mid]