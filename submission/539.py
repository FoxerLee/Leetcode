class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints = sorted(timePoints)
        
        dif = float('inf')
        for i in range(len(timePoints)-1):
            time1 = int(timePoints[i][0:2])*60 + int(timePoints[i][3:5])
            time2 = int(timePoints[i+1][0:2])*60 + int(timePoints[i+1][3:5])
            
            dif = min(dif, int(time2) - int(time1))
            
        time1 = timePoints[len(timePoints)-1][0:2] + timePoints[len(timePoints)-1][3:5]
        time2 = timePoints[0][0:2] + timePoints[0][3:5]
        
        tmp = (23 - int(time1[0:2]))*60 + (60 - int(time1[2:4])) + (int(time2[0:2]))*60 + int(time2[2:4])
        
        dif = min(dif, tmp)
        
        return dif
            
            
