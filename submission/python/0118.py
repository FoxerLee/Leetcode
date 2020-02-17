class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # if numRows < 1:
        #     return [[1]]

        res = []
        for i in range(numRows):
            res.append([0 for _ in range(i+1)])

        for i in range(len(res)):
            if i == 0:
                res[i][0] = 1

            else:
                for j in range(len(res[i])):
                    if j == 0 or j == len(res[i])-1:
                        res[i][j] = 1
                    else:
                        res[i][j] = res[i-1][j-1] + res[i-1][j]
            
        return res
