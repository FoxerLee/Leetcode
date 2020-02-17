class Solution:
    def helper(self, left, right, up, down, matrix, target):
        if left > right or up > down:
            return False
        elif target < matrix[up][left] or target > matrix[down][right]:
                return False
        
        mid = left + (right-left)//2
        
        tmp = up
        
        while tmp <= down and matrix[tmp][mid] <= target:
            if matrix[tmp][mid] == target:
                return True
            tmp += 1
        
        return self.helper(left, mid-1, tmp, down, matrix, target) or self.helper(mid+1, right, up, tmp-1, matrix, target)
        
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        
        return self.helper(0, len(matrix[0])-1, 0, len(matrix)-1, matrix, target)
        
        
        
