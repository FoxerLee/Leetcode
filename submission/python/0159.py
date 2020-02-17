class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        chars = collections.defaultdict()
        ans = 0
        
        p1 = 0
        p2 = 0
        
        while p2 < len(s):
            if len(chars) < 3:
                chars[s[p2]] = p2
                p2 += 1
                
            if len(chars) == 3:
                de_needed = min(chars.values())
                del chars[s[de_needed]]
                p1 = de_needed + 1
                
            ans = max(ans, p2-p1)
            
        return ans
