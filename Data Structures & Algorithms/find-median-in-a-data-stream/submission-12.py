import heapq

class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        heapq.heappush_max(self.maxHeap, num)
        if self.minHeap and self.maxHeap[0] > self.minHeap[0]:
            curr = heapq.heappop_max(self.maxHeap)
            heapq.heappush(self.minHeap, curr)

        if abs(len(self.minHeap) - len(self.maxHeap)) > 1:
            self.equalize()

    def equalize(self):
        if len(self.minHeap) > len(self.maxHeap):
            curr = heapq.heappop(self.minHeap)
            heapq.heappush_max(self.maxHeap, curr)
        else:
            curr = heapq.heappop_max(self.maxHeap)
            heapq.heappush(self.minHeap, curr)

    def findMedian(self) -> float:
        if len(self.minHeap) == len(self.maxHeap):
            return (self.minHeap[0] + self.maxHeap[0]) / 2.0
        else:
            return self.minHeap[0] if len(self.minHeap) > len(self.maxHeap) else self.maxHeap[0]