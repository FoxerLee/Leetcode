class DSU:
    def __init__(self):
        self.p = [i for i in range(1500)]
        self.r = [0 for _ in range(1500)]
        
    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
            
        return self.p[x]
    
    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        
        if xr == yr:
            return False
        elif self.r[xr] < self.r[yr]:
            self.p[xr] = yr
            self.r[yr] += 1
        elif self.r[xr] > self.r[yr]:
            self.p[yr] = xr
            self.r[xr] += 1
        else:
            self.p[yr] = xr
            self.r[xr] += 1
            
        return True
        
        

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU()
        for edge in edges:
            if not dsu.union(edge[0], edge[1]):
                return edge
