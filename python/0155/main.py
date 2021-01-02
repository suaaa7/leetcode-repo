class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_val = float("inf")

    def push(self, x: int) -> None:
        self.stack.append(x)
        if x < self.min_val:
            self.min_val = x

    def update_min(self):
        self.min_val = min(self.stack) if len(self.stack) > 0 else float("inf")

    def pop(self) -> None:
        item = self.stack.pop()
        if item == self.min_val:
            self.update_min()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_val


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
