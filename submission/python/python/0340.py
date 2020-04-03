class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        char_dict = collections.defaultdict(int)

        l = 0
        r = 0
        dif = 0
        ans = 0
        while l < len(s) and r < len(s):
            if s[r] not in char_dict or char_dict[s[r]] == 0:
                dif += 1
            char_dict[s[r]] += 1
            

            while dif > k:
                char_dict[s[l]] -= 1
                if char_dict[s[l]] == 0:
                    dif -= 1
                l += 1

            ans = max(ans, r - l + 1)
            r += 1

        return ans
