class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:        
        rows = len(mat)
        
        hash_table = collections.defaultdict(int)
        
        for i in range(rows-1):
            m = mat[i]
            for num in m:
                hash_table[num] += 1
                
        for num in mat[-1]:
            if hash_table[num] + 1 == rows:
                return num
            
        return -1
