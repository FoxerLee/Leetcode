class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        if not preorder:
            return True
        
        cnk, stack = None, []
        for n in preorder:
            while stack and stack[-1] < n:
                cnk = stack.pop()
            if cnk != None and n < cnk:
                return False
            stack.append(n)
            
        return True
                
            
