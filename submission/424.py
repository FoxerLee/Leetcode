class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_dict = collections.defaultdict(int)
        
        l = 0
        r = 0
        
        max_value = 0
        max_char = ''
        ans = 0
        while l < len(s) and r < len(s):
            char_dict[s[r]] += 1
            
            if char_dict[s[r]] > max_value:
                max_value = char_dict[s[r]]
                max_char = s[r]
            
            if max_value + k >= r - l + 1:
                ans = r - l + 1
            else:
                char_dict[s[l]] -= 1
                if s[l] == max_char:
                    max_value -= 1
                l += 1
            
            
            r += 1
                
        return ans
            
            
