class Solution:
    def shortestWordDistance(self, words: List[str], word1: str, word2: str) -> int:
        loc = collections.defaultdict(list)
        
        for i, word in enumerate(words):
            loc[word].append(i)
            
        loc1 = loc[word1]
        loc2 = loc[word2]
        
        ans = float("inf")
        l = 0
        r = 0
        while l < len(loc1) and r < len(loc2):
            if abs(loc2[r]-loc1[l]) != 0:
                ans = min(ans, abs(loc2[r]-loc1[l]))
            if loc1[l] < loc2[r]:
                l += 1
            else:
                r += 1
                
        return ans
