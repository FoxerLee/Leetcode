class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        _map = collections.defaultdict(int)
        
        for a in arr:
            _map[a] += 1
            
        values = _map.values()
        values = sorted(values)
        
        for i in range(len(values)-1):
            if values[i] == values[i+1]:
                return False
            
        return True
        
        
