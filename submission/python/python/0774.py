class Solution:
    def minmaxGasDist(self, stations: List[int], K: int) -> float:
        l, r = 0, max(stations)
        
        while r - l > 1e-6:
            D = (l+r) / 2.0
            if sum(int((stations[i+1] - stations[i]) / D) for i in range(len(stations)-1)) > K:
                l = D
            else:
                r = D
                
        return l
