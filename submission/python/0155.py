class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = float('inf')

    def push(self, x: int) -> None:
        if x < self.min:
            self.min = x
        self.stack.append(x)

    def pop(self) -> None:
        ele = self.stack.pop()
        if ele == self.min:
            if self.stack != []:
                self.min = min(self.stack)
            else:
                self.min = float('inf')

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
