class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        # points.sort()
        S = set(map(tuple, points))
        ans = float('inf')
        for i, p1 in enumerate(points):
            for j in range(i):
                p2 = points[j]
                if p1[0] != p2[0] and p1[1] != p2[1]:
                    if (p1[0], p2[1]) in S and (p2[0], p1[1]) in S:
                        tmp = abs(p2[1] - p1[1])*abs(p2[0] - p1[0])
                        if tmp < ans:
                            ans = tmp
        return ans if ans != float('inf') else 0
        
        
