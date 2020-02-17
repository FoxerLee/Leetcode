class Solution:
    def firstUniqChar(self, s: str) -> int:
        if s == "":
            return -1
        char_dict = collections.defaultdict(list)
        for i in range(len(s)):
            char_dict[s[i]].append(i)
            
        sort_fre = sorted(char_dict.values(), key=lambda value: len(value))
        
        idx = float('inf')
        for f in sort_fre:
            if len(f) > 1:
                break
            if f[0] < idx:
                idx = f[0]
        
        return idx if idx != float('inf') else -1
            
