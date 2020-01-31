class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if s == []:
            return []
        n = len(s) - 1
        for i in range(len(s)//2):
            tmp = s[i]
            s[i] = s[n-i]
            s[n-i] = tmp
            
        
