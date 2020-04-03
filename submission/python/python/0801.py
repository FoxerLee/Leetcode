class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        N = len(A)
        no, swap = N*[N], N*[N]
        no[0], swap[0] = 0, 1
        
        for i in range(1, N):
            if A[i-1] < A[i] and B[i-1] < B[i]:
                no[i] = no[i-1]
                swap[i] = swap[i-1] + 1
                
            if A[i-1] < B[i] and B[i-1] < A[i]:
                no[i] = min(no[i], swap[i-1])
                swap[i] = min(no[i-1]+1, swap[i])
                
        return min(swap[-1], no[-1])
        
