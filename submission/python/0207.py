class Solution:
    def dfs(self, visited, adj, node, res):
        visited[node] = 1
        for nei in adj[node]:
            if visited[nei] == 1:
                return False
            elif visited[nei] == 0:
                if not self.dfs(visited, adj, nei, res):
                    return False
        visited[node] = 2
        return True
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {}
        visited = {}
        
        for n in range(numCourses):
            adj[n] = set()
            visited[n] = 0
        
        # generate graph
        for pre in prerequisites:
            adj[pre[0]].add(pre[1])
        
        res = True
        for c in visited:
            if visited[c] == 0:
                if not self.dfs(visited, adj, c, res):
                    return False
        
        return True
