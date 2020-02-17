class Solution:
    def confusingNumber(self, N: int) -> bool:
        cn = set(['0', '1', '6', '8', '9'])
        N = str(N)
        for n in N:
            if n not in cn:
                return False
        
        if len(N) == 1:
            if N == '6' or N == '9':
                return True
            else:
                return False
        
        N_re = N[::-1]
        
        
        for i in range(len(N)):
            if N[i] == N_re[i] == '8' or N[i] == N_re[i] == '1' or N[i] == N_re[i] == '0' or (N[i] == '6' and N_re[i] == '9') or (N[i] == '9' and N_re[i] == '6'):
                continue
            else:
                return True
        
        
        return False
