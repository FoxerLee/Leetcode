class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res =[0]
        for i in range(n):
            res += [x + pow(2, i) for x in reversed(res)]
            
        return res
