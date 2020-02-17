class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        ans = []
        # right
        x = king[0]
        y = king[1]
        while x < 8:
            if [x,y] in queens:
                ans.append([x,y])
                break
            x += 1
        
        # r-b
        x = king[0]
        y = king[1]
        while x < 8 and y < 8:
            if [x,y] in queens:
                ans.append([x,y])
                break
            x += 1
            y += 1
            
        x = king[0]
        y = king[1]
        while y < 8:
            if [x,y] in queens:
                ans.append([x,y])
                break
            y += 1
            
        
        x = king[0]
        y = king[1]
        while x >= 0 and y < 8:
            if [x,y] in queens:
                ans.append([x,y])
                break
            x -= 1
            y += 1
            
        x = king[0]
        y = king[1]
        while x >= 0:
            if [x,y] in queens:
                ans.append([x,y])
                break
            x -= 1
            
        x = king[0]
        y = king[1]
        while x >= 0 and y >= 0:
            if [x,y] in queens:
                ans.append([x,y])
                break
            x -= 1
            y -= 1
            
            
        x = king[0]
        y = king[1]
        while y >= 0:
            if [x,y] in queens:
                ans.append([x,y])
                break
            y -= 1
            
        
        x = king[0]
        y = king[1]
        while y >= 0 and x < 8:
            if [x,y] in queens:
                ans.append([x,y])
                break
            y -= 1
            x += 1
            
        return ans
                
            
