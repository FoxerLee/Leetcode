class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtrack(row):
            for col in range(n):
                if not (rows[col] or diag1[row-col] or diag2[row+col]):
                    queens.add((row, col))
                    rows[col] = 1
                    diag1[row-col] = 1
                    diag2[row+col] = 1
                    
                    if row+1 == n:
                        tmp = []
                        for _, col in sorted(queens):
                            tmp.append('.' * col + 'Q' + '.' * (n - col - 1))
                        ans.append(tmp)
                    else:
                        backtrack(row+1)
                    queens.remove((row, col))
                    rows[col] = 0
                    diag1[row-col] = 0
                    diag2[row+col] = 0
                
            return ans
                    
        
        rows = [0 for _ in range(n)]
        diag1 = [0 for _ in range(2*n-1)]
        diag2 = [0 for _ in range(2*n-1)]
        queens = set()
        ans = []
        backtrack(0)
        return ans
