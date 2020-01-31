class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = collections.deque()
        R = len(grid)
        C = len(grid[0])
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
        
        
        
        
        ans = 0
        while queue:
            r, c, ans = queue.popleft()
            
            for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                if 0 <= nr < R and 0 <= nc < C:
                    if grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        queue.append((nr, nc, ans+1))
                        
        
        for row in grid:
            if 1 in row:
                return -1
            
        return ans
