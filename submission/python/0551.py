class Solution:
    def checkRecord(self, s: str) -> bool:
        if s == "":
            return True
        
        
        a_c = 0
        l_c = 0
        for c in s:
            if c == "A":
                a_c += 1
                if a_c > 1:
                    return False
            if c == "L":
                l_c += 1
                if l_c > 2:
                    return False
            else:
                l_c = 0
                
                
        return True
                
            
        
        
