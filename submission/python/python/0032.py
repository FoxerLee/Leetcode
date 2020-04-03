class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        max_ans = 0
        stack = []
        
        stack.append(-1)
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                peek = stack.pop()
                if stack == []:
                    stack.append(i)
                else:
                    max_ans = max(max_ans, i-stack[-1])
                    
        return max_ans
