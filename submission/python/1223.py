class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        l = len(rollMax)
        dp = [[0 for i in range(l + 1)] for j in range(n + 1)]
        
        dp[0][l] = 1
        dp[1][l] = l
        for j in range(l):
            dp[1][j] = 1

        for i in range(2, n + 1):          
            for j in range(l):              
                for k in range(1, rollMax[j] + 1):
                    if i - k < 0:
                        break
                    dp[i][j] = dp[i][j] - dp[i - k][j] + dp[i - k][l] 
            dp[i][l] = sum(dp[i])
        
        return dp[n][l] % 1000000007
