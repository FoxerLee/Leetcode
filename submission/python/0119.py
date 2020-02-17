class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # res = []
#         for i in range(rowIndex+1):
#             res.append([0 for _ in range(i+1)])

#         for i in range(len(res)):
#             if i == 0:
#                 res[i][0] = 1

#             else:
#                 for j in range(len(res[i])):
#                     if j == 0 or j == len(res[i])-1:
#                         res[i][j] = 1
#                     else:
#                         res[i][j] = res[i-1][j-1] + res[i-1][j]
                        
#         return res[-1]

        res = []
        for i in range(rowIndex+1):
            
            if i == 0 or i == 1:
                res.append(1)
            else:
                for j in range(len(res)-1, 0, -1):
                    res[j] = res[j] + res[j-1]
                res.append(1)
                
        return res
                    
