class Solution:
    
    def dfs(self, s, cnt):
        while s < len(self.debt) and self.debt[s] == 0:
            s += 1

        res = float('inf')
        prev = 0
        for j in range(s+1, len(self.debt)):
            if self.debt[j] != prev and self.debt[j]*self.debt[s] < 0:
                self.debt[j] += self.debt[s]
                res = min(res, self.dfs(s+1, cnt+1))
                self.debt[j] -= self.debt[s]
                prev = self.debt[j]

        return res if res < float('inf') else cnt

    
    def minTransfers(self, transactions: List[List[int]]) -> int:
        account = collections.defaultdict(int)
        
        for t in transactions:
            account[t[0]] -= t[2]
            account[t[1]] += t[2]
            
        self.debt = []
        for value in account.values():
            if value != 0:
                self.debt.append(value)
                
        
            
        
        return self.dfs(0, 0)
