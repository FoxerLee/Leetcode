class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        if n == 0:
            return [""]
        tmp1 = ['0', '1', '8']
        tmp2 = ['11', '69', '88', '96', '00']
        
        if n == 1:
            return tmp1
        if n == 2:
            return tmp2[:-1]
        
        if n % 2 != 0:
            pre = self.findStrobogrammatic(n-1)
            mid = tmp1
            
        else:
            pre = self.findStrobogrammatic(n-2)
            mid = tmp2
            
        pre_mid = int((n-1)/2)
        return [can[:pre_mid] + c + can[pre_mid:] for c in mid for can in pre]
            
            
                
