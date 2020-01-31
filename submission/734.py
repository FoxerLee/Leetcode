class Solution:
    def areSentencesSimilar(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        if len(words1) != len(words2):
            return False
        
        pairset = set(map(tuple, pairs))
        
        for w1, w2 in zip(words1, words2):
            if w1 != w2 and (w1, w2) not in pairset and (w2, w1) not in pairset:
                return False
            
        return True
