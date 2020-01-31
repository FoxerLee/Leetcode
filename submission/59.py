class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [([0] * n) for i in range(n)]
        i, j, di, dj = 0, 0, 0, 1
        for k in range(1, n * n+1):
            res[i][j] = k
            if i + di >= n or j + dj >= n or res[i + di][j + dj] != 0:
                di, dj = dj, -di

            i += di
            j += dj
        return res
        
        
