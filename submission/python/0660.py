class Solution:
    def newInteger(self, n: int) -> int:
        b = []
        while True:
            tmp = n // 9
            y = n % 9
            b += [y]
            if tmp == 0:
                break
            n = tmp
        
        b.reverse()
        res = ""
        
        for i in b:
            res += str(i)
            
        return int(res)
