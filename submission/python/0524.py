class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
       
        # d = sorted(d, key=lambda x: len(x))
        d = sorted(d)
        # d.reverse()
        ans = ""
        
        # print(d)

        for word in d:
            ps = 0
            pw = 0
            while ps < len(s) and pw < len(word):
                if word[pw] == s[ps]:
                    ps += 1
                    pw += 1
                else:
                    ps += 1
            if pw == len(word) and ps <= len(s):
                if len(ans) < len(word):
                    ans = word

        return ans
