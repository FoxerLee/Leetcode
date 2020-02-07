from heapq import *
class MedianFinder:

    def __init__(self):
        self.lo = []  
        self.hi = []

    def addNum(self, num):
        # if len(self.small) == len(self.large):
        heappush(self.hi, -heappushpop(self.lo, -num))
        
        while len(self.hi) > len(self.lo):
            heappush(self.lo, -heappop(self.hi))
            # heappush(self.small, -heappushpop(self.large, num))

    def findMedian(self):
        if len(self.lo) == len(self.hi):
            return float(self.hi[0] - self.lo[0]) / 2.0
        else:
            return float(-self.lo[0])
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
