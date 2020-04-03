class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_s = collections.defaultdict(int)
        
        for char in s:
            hash_s[char] += 1
        
        for char in t:
            hash_s[char] -= 1
            
        for v in hash_s.values():
            if v != 0:
                return False
        return True
