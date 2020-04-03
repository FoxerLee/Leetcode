class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows = [sum(row) for row in grid]
        cols = []
        for i in range(len(grid[0])):
            _sum = 0
            for j in range(len(grid)):
                _sum += grid[j][i]
            cols.append(_sum)
            
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if rows[i] + cols[j] > 2 and grid[i][j]:
                    ans += 1
        return ans
