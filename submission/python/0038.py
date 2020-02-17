class Solution:
    def countAndSay(self, n: int) -> str:
        ans = '1'
        
        for _ in range(n-1):
            tmp = ''
            for digit, group in itertools.groupby(ans):
                tmp += str(len(list(group))) + digit
            ans = tmp
            
        return ans
