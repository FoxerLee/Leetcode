

class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        
        v1 = [points[0][0] - points[1][0], points[0][1] - points[1][1]]
        v2 = [points[0][0] - points[2][0], points[0][1] - points[2][1]]
        
        return False if v2[0]*v1[1] - v2[1]*v1[0] == 0.0 else True
                       
