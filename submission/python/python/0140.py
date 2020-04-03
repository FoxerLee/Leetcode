class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        dp = [[] for _ in range(len(s)+1)]
        dp[0].append("")
        for i in range(len(s)):
            if len(dp[i]) == 0:
                continue
            for word in wordDict:
                if word == s[i:i + len(word)]:
                    dp[i + len(word)].append(word)
                    
        results = []
        
        
        def dfs(path, pos):
            if pos == 0:
                results.append(" ".join(reversed(path)))
                return
            
            for word in dp[pos]:
                path.append(word)
                dfs(path, pos - len(word))
                path.pop()
        
        dfs([], len(dp) - 1)
                
        return results
