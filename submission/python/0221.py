class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if matrix == [] or matrix[0] == []:
            return 0
        dp = [[0 for _ in range(len(matrix[0])+1)] for _ in range(len(matrix)+1)]
        
        maxLen = 0
        
#         for i in range(len(matrix)):
#             if matrix[i][0] == '1':
#                 dp[i][0] = 1

#         for i in range(len(matrix[0])):
#             if matrix[0][i] == '1':
#                 dp[0][i] = 1
                
        for i in range(1, len(matrix)+1):
            for j in range(1, len(matrix[0])+1):

                if matrix[i-1][j-1] == '1':
                    dp[i][j] = min(min(dp[i-1][j], dp[i][j-1]), dp[i-1][j-1]) + 1
                if maxLen < dp[i][j]:
                        maxLen = dp[i][j]
                            
        return maxLen**2
              
              
