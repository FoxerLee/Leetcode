class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        if n <= 1:
            return []
        ans = []
        
        def dfs(path, num, n):
            if len(path) > 0:
                ans.append(path+[n])
                
            for i in range(num, int(math.sqrt(n)+1)):
                if n % i == 0:
                    dfs(path+[i], i, n//i)
        dfs([], 2, n)          
        return ans
