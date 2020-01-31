class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        power = 5
        while n//power:
            count += n//power
            power *= 5
            
        return count
