class Solution:
    def getStr(self, stack):
        string = ""
        c = stack.pop()
        while c != "[":
            string = c + string
            c = stack.pop()
        
        nums = ""
        # c = stack.pop()
        while stack != [] and stack[-1].isdigit():
           
            c = stack.pop()
            nums = c + nums
            
        # stack.append(c)
        
        for _ in range(int(nums)):
            stack.append(string)
        
    
    def decodeString(self, s: str) -> str:
        if s == "":
            return ""
        
        i = 0
        stack = []
        while i < len(s):
            if s[i] != ']':
                stack.append(s[i])
            else:
                self.getStr(stack)
            i += 1
            
        return "".join(stack)
            
        
