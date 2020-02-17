class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_len = len(s)
        p_len = len(p)
        dp = [[False for _ in range(s_len+1)] for _ in range(p_len+1)]
        dp[0][0] = True
        
        for i in range(1, p_len+1):
            
            if p[i-1] == '*':
                j = 1
                while not dp[i-1][j-1] and j < s_len+1:
                    j += 1
                dp[i][j-1] = dp[i-1][j-1]
                
                while j < s_len+1:
                    dp[i][j] = True
                    j += 1
            elif p[i-1] == '?':
                for j in range(1, s_len+1):
                    dp[i][j] = dp[i-1][j-1]
            else:
                for j in range(1, s_len+1):
                    dp[i][j] = (p[i-1] == s[j-1] and dp[i-1][j-1])
                        # dp[i][j] = True
                        
        return dp[p_len][s_len]
                        
