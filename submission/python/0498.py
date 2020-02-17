class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return None
        if not matrix[0]:
            return None
        
        new_matrix = []
        
        row = 0
        col = 0
        i = 0
        
        while i < len(matrix)*len(matrix[0]):
            new_matrix.append(matrix[row][col])
            if (row + col) % 2 == 0:
                if col == len(matrix[0]) - 1:
                    row += 1
                elif row == 0:
                    col += 1
                else:
                    row -= 1
                    col += 1
            else:
                if row == len(matrix) - 1:
                    col += 1
                elif col == 0:
                    row += 1
                else:
                    row += 1
                    col -= 1

            i += 1

        return new_matrix
            
