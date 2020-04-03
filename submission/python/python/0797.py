class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        def dfs(i):
            if i == len(graph) - 1:
                return [[i]]
            ans = []
            for j in graph[i]:          
                for nei in dfs(j):
                    ans.append([i] + nei)
            return ans
                
        
        return dfs(0)
