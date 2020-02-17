class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        
        p2s = {}
        s2p = {}
        str_l = str.split(" ")
        
        if len(str_l) != len(pattern):
            return False
        
        for i in range(len(pattern)):
            if pattern[i] not in p2s:
                p2s[pattern[i]] = str_l[i]
            else:
                if p2s[pattern[i]] != str_l[i]:
                    return False
            if str_l[i] not in s2p:
                s2p[str_l[i]] = pattern[i]
            else:
                if s2p[str_l[i]] != pattern[i]:
                    return False
                
        return True
