class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_table = set()
        
        i = 0
        j = 0
        ans = 0
        while i < len(s) and j < len(s):
            if s[j] not in hash_table:
                hash_table.add(s[j])
                j += 1
                ans = max(ans, j-i)
            else:
                hash_table.remove(s[i])
                i += 1
                
        return ans
