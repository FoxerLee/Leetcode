class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        ans = 1
        s_p = 0
        t_p = 0
        
        while t_p < len(target):
            tmp_p = s_p
            while s_p < len(source) and target[t_p] != source[s_p]:
                s_p += 1
            
            if s_p == len(source):
                ans += 1
                s_p = 0
                while s_p < tmp_p and target[t_p] != source[s_p]:
                    s_p += 1
                if s_p == tmp_p:
                    return -1
            s_p += 1
            t_p += 1
            
        return ans
                
