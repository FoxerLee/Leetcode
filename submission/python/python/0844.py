class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        
        long = len(S)-1
        skip = 0
        tmp_s = ""
        for i in range(long, -1, -1):
            if S[i] == '#':
                skip += 1
            elif skip > 0:
                skip -= 1
            else:
                tmp_s = S[i] + tmp_s
         
        long = len(T)-1
        skip = 0
        tmp_t = ""
        for i in range(long, -1, -1):
            if T[i] == '#':
                skip += 1
            elif skip > 0:
                skip -= 1
            else:
                tmp_t = T[i] + tmp_t
                
        return tmp_s == tmp_t
        
            
