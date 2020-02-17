class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        words = collections.defaultdict(int)
        
        for i in range(0, len(s)-minSize+1):
            word = s[i:i+minSize]
            a = collections.Counter(word)
            if len(collections.Counter(word)) <= maxLetters:
                words[word] += 1
                
        return max(words.values()) if len(words) != 0 else 0
