class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations:
            return 0
        citations = sorted(citations)
        
        for i in range(len(citations)):
            h = len(citations) - i
            if h <= citations[i]:
                return h
            
        return 0
