from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if s == '' or words == []:
            return []
        
        ans = []
        
        word_c = len(words)
        word_l = len(words[0])
        
        window_s = word_c*word_l
        
        for i in range(0, len(s)-window_s+1):
            window = s[i:window_s+i]
            
            cur_words = []
            for j in range(0, window_s, word_l):
                cur_words.append(window[j:j+word_l])
                
            if Counter(cur_words) == Counter(words):
                ans.append(i)
                
        return ans
            
            
