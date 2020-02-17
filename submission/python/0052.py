class Solution:
    def totalNQueens(self, n: int) -> int:
        # ans = 0
        
        def backtrack(row, ans):
            for col in range(n):
                if not (rows[col] or diag1[row-col] or diag2[row+col]):
                    rows[col] = 1
                    diag1[row-col] = 1
                    diag2[row+col] = 1
                    
                    if row+1 == n:
                        ans += 1
                    else:
                        ans = backtrack(row+1, ans)
                    rows[col] = 0
                    diag1[row-col] = 0
                    diag2[row+col] = 0
                
            return ans
                    
        
        rows = [0 for _ in range(n)]
        diag1 = [0 for _ in range(2*n-1)]
        diag2 = [0 for _ in range(2*n-1)]
        
        return backtrack(0, 0)
