class Solution:

    def __init__(self, w: List[int]):
        self.index_w = [0]*len(w)
        self.sum = 0
        for i in range(len(w)):
            self.sum += w[i]
            self.index_w[i] = self.sum
        
    def pickIndex(self) -> int:
        idx = random.randint(1, self.sum)
        
        l = 0
        r = len(self.index_w)
        
        while l < r:
            mid = (l+r)//2
            if idx == self.index_w[mid]:
                return mid
            elif idx > self.index_w[mid]:
                l = mid + 1
            else:
                r = mid
            
        return l
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
