class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        l = -1
        r = -1
        
        ans = len(words)
        for i in range(len(words)):
            if words[i] == word1:
                l = i
                
            elif words[i] == word2:
                r = i
                
            if l != -1 and r != -1:
                ans = min(abs(r-l), ans)
                
        return ans
