class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = []
        while matrix != []:
            result += matrix.pop(0)
            if matrix and matrix[0]:
                for r in matrix:
                    result.append(r.pop())
            if matrix:
                result += matrix.pop()[::-1]
            if matrix and matrix[0]:
                for r in matrix[::-1]:
                    result.append(r.pop(0))
        return result
                    
