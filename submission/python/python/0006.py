class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 0 or s == "":
            return ""
        if numRows == 1:
            return s
        
        res = [[] for _ in range(numRows)]
        delta = 1
        temp = 0

        for c in s:

            if delta == 1 and temp < numRows-1:
                res[temp].append(c)
                temp += 1
            elif delta == 1 and temp == numRows-1:
                res[temp].append(c)
                temp -= 1
                delta = -1
            elif delta == -1 and temp > 0:
                res[temp].append(c)
                temp -= 1
            elif delta == -1 and temp == 0:
                res[temp].append(c)
                temp += 1
                delta = 1

        res_str = ""
        for i in range(numRows):
            for j in range(len(res[i])):
                res_str += res[i][j]
                
        return res_str
        
