class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:
        l_max = [0] * len(A)
        r_min = [0] * len(A)
        
        _max = A[0]
        for i in range(len(A)):
            _max = max(_max, A[i])
            l_max[i] = _max
            
        _min = A[-1]
        for i in range(len(A)-1, -1, -1):
            _min = min(_min, A[i])
            r_min[i] = _min
            
        for i in range(1, len(A)):
            if l_max[i-1] <= r_min[i]:
                return i
