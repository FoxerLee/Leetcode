class Solution:
    def cal_fre(self, s):
        s = sorted(s)
        length = 1
        s_char = s[0]
        i = 1
        while i < len(s):
            if s[i] == s_char:
                length += 1
            else:
                break
            i += 1
        return length
    
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        q_len = []
        for q in queries:
            length = self.cal_fre(q)
            q_len.append(length)
        
        w_len = []
        for w in words:
            length = self.cal_fre(w)
            w_len.append(length)
        
        ans = []
        for q in q_len:
            tmp = 0
            for w in w_len:
                if q < w:
                    tmp += 1
            ans.append(tmp)
            
        return ans
            
