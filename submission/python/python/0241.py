class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        if input.isdigit():
            return [int(input)]
        
        ans = []
        for i in range(len(input)):
            if input[i] in ['+', '-', '*']:
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[i+1:])
                
                for n in left:
                    for m in right:
                        ans.append(self.help(n, m, input[i]))
                        
        return ans
    
    def help(self, n, m, op):
        if op == '-':
            return n - m
        if op == '+':
            return n + m
        if op == '*':
            return n * m
