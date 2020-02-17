class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict_set = set(wordDict)
        
        queue = []
        
        queue.append(0)
        visited = [0 for _ in range(len(s))]
        while queue:
            start = queue.pop(0)
            if visited[start] == 0:
                for i in range(start+1, len(s)+1):
                    if s[start:i] in wordDict_set:
                        if i == len(s):
                            return True
                        queue.append(i)
                visited[start] = 1
            
        return False
            
