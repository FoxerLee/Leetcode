class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if s == "" and t == "":
            return True
        
        dic_s = collections.defaultdict(str)
        
        
        for i in range(len(t)):
            if not s[i] in dic_s:
                dic_s[s[i]] = t[i]
            else:
                if dic_s[s[i]] != t[i]:
                    return False
                
        dic_t = collections.defaultdict(str)
        for i in range(len(t)):
            if not t[i] in dic_t:
                dic_t[t[i]] = s[i]
            else:
                if dic_t[t[i]] != s[i]:
                    return False
                
        return True
