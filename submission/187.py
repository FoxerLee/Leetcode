class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        hash_dna = collections.defaultdict(str)
        
        ans = set()
        for i in range(0, len(s)-9):
            tmp = s[i:i+10]
            if tmp in hash_dna.keys():
                ans.add(tmp)
            else:
                hash_dna[tmp] = "True"
                
        return list(ans)
            
        
