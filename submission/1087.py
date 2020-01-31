class Solution:
    def expand(self, S: str) -> List[str]:
        helper = []
        
        i = 0
        while i < len(S):
            if S[i] == '{':
                tmp = []
                i += 1
                while S[i] != '}':
                    if S[i] == ',':
                        i += 1
                        continue
                    tmp.append(S[i])
                    i += 1
                
                helper.append(tmp)
                i += 1
            else:
                helper.append(S[i])
                i += 1
        
        ans = [""]
        
        for cs in helper:
            cur = []
            for c in cs:
                for word in ans:
                    cur.append(word+c)
            ans = cur[:]
            
        return sorted(list(set(ans)))
