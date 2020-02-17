class Solution:
    def graph(self, words, visited, adj):
        for word in words:
            for c in word:
                visited[c] = 0
                adj[c] = set()
        
        
        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]
            diff = False
            for j in range(min(len(w1), len(w2))):
                if w1[j] != w2[j]:
                    diff = True
                    adj[w1[j]].add(w2[j])
                    break
                j += 1
            if not diff and len(w1) > len(w2):
                return False
        return True
    
    def dfs(self, visited, adj, c, res):
        
        visited[c] = 1
        for nei in adj[c]:
            if visited[nei] == 1:
                return False
            elif visited[nei] == 0:
                if not self.dfs(visited, adj, nei, res):
                    return False
        res.append(c)
        visited[c] = 2
        
        return True
                         
    
    
    def alienOrder(self, words: List[str]) -> str:
        visited = {}
        adj = {}
        
        if not self.graph(words, visited, adj):
            return ""
        
        res = []
        for c in visited:
            if visited[c] == 0:
                # return False if the graph is cyclic
                if not self.dfs(visited, adj, c, res):
                    
                    return ""
        return "".join(reversed(res))
        
