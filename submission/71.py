class Solution:
    def simplifyPath(self, path: str) -> str:
        if path == '':
            return ''
        stack = []
        split_path = path.split('/')
        
        for p in split_path:
            if p == '' or p == '.':
                continue
            elif p == '..' and stack:
                stack.pop()
            elif p != '..' and p != '.':
                stack.append(p)
                
        ans = ""
        while stack:
            ans += '/'+stack.pop(0)
            
        return ans if ans != '' else '/'
