from numpy import stack


class MinStack:

    def __init__(self):
        self.stack = [] # containes (minofstack, elem)
        

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
        else:
            mn, v = self.stack[-1]
            minOfStack = min(mn, val)
            self.stack.append((minOfStack, val))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        mn, val = self.stack[-1]
        return val

    def getMin(self) -> int:
        mn, val = self.stack[-1]
        return mn


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()