class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return 0
        d = {char: i+1 for i, char in enumerate(string.ascii_uppercase) }
        # digit = 0
        
        res = 0
        # s = sorted(s)
        # while s != []:
        #     tmp = s.pop()
        #     res += (ord(tmp) - base)*(26**digit)
        #     digit += 1
        length = len(s)
        for i, char in enumerate(s):
            res += d[char]*(26**(length-i-1))
        return res
