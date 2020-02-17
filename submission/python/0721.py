class DSU:
    def __init__(self):
        self.p = [i for i in range(20000)]
        self.r = [0 for _ in range(20000)]
        
    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]
    
    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        
        if xr == yr:
            # return False
            return
        elif self.r[xr] < self.r[yr]:
            self.p[xr] = yr
            self.r[yr] += 1
        elif self.r[xr] > self.r[yr]:
            self.p[yr] = xr
            self.r[xr] += 1
        else:
            self.p[yr] = xr
            self.r[xr] += 1
            
        # return True
    # def union(self, x, y):
    #     self.p[self.find(x)] = self.find(y)
    

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        dsu = DSU()
        email_name = collections.defaultdict(str)
        email_id = collections.defaultdict(int)
        tmp = 0
        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                if email not in email_id:
                    email_id[email] = tmp
                    tmp += 1
                email_name[email] = name
                
                dsu.union(email_id[acc[1]], email_id[email])
            
        ans = collections.defaultdict(list)
        
        for email in email_name:
            ans[dsu.find(email_id[email])].append(email)
            
        return [[email_name[value[0]]] + sorted(value) for value in ans.values()]
