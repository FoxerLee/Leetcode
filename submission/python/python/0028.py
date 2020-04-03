class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        j = 0
        count = 0

        while i < len(haystack) and j < len(needle):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
                count += 1
            elif haystack[i] != needle[j]:
                count = 0
                i = i - j + 1
                j = 0
        

        if j >= len(needle):
            return i-count
        else:
            return -1
