class MyQueue:

    def __init__(self):
        self.inComingStack = []
        self.outGoingStack = []
        

    def push(self, x: int) -> None:
        self.inComingStack.append(x)

    def pop(self) -> int:
        if self.outGoingStack:
            return self.outGoingStack.pop()
        else:
            while self.inComingStack:
                self.outGoingStack.append(self.inComingStack.pop())
            return self.outGoingStack.pop()

    def peek(self) -> int:
        if self.outGoingStack:
            return self.outGoingStack[-1]
        else:
            while self.inComingStack:
                self.outGoingStack.append(self.inComingStack.pop())
            return self.outGoingStack[-1]
        
    def empty(self) -> bool:
        return len(self.inComingStack) + len(self.outGoingStack) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()