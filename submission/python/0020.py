class Solution:
    def isValid(self, s: str) -> bool:
        stack = ['#']
        
        hash_map = {"}": "{", ")" : "(", "]":"["}
        
        for c in s:
            if c in hash_map:
                top = stack.pop()
                
                if hash_map[c] != top:
                    return False
                
            else:
                stack.append(c)
                
        if stack == ['#']:
            return True
        else:
            return False
                
