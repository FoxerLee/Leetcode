class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return 0
        res = [0 for x in range(len(s)+1)]
        res[0] = 1
        
        for i in range(1, len(s)+1):
            if s[i-1] != '0':
                res[i] += res[i-1]
            if i != 1 and s[i-2:i] > '09' and s[i-2:i] < '27':
                res[i] += res[i-2]
                
        return res[-1]
        
