class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = []
        if n % 2 == 1:
            n = n - 1
            ans.append(0)
            
        tmp = 1
        for _ in range(int(n/2)):
            ans.append(tmp)
            ans.append(-tmp)
            tmp += 1
            
        return ans
