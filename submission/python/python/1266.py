class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        pre = points[0]
        ans = 0
        
        for i in range(1, len(points)):
            des = points[i]
            ans += max(abs(des[0]-pre[0]), abs(des[1]-pre[1]))
                
            pre = points[i]
            
        return ans
