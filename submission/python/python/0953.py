class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alien_dict = collections.defaultdict(int)
        
        for i in range(len(order)):
            char = order[i]
            alien_dict[char] = i
            
        
        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]
            
            
            for j in range(min(len(word1), len(word2))):
                if word1[j] != word2[j]:
                    if alien_dict[word1[j]] > alien_dict[word2[j]]:
                        return False  
                    break
            else:      
                if len(word1) > len(word2):
                    return False
                    
        return True
                
            
