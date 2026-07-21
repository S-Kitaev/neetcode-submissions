class MinStack:

    def __init__(self):
        self.min_num = 2**31 - 1
        self.stack = []

    def push(self, val: int) -> None:
        self.stack = [val] + self.stack
        if self.min_num > val:
            self.min_num = val
        
    def pop(self) -> None:
        self.stack = self.stack[1:]
        if len(self.stack) == 0:
            self.min_num = 2**31 - 1
        else:
            self.min_num = min(self.stack)
        
    def top(self) -> int:
        return self.stack[0]

    def getMin(self) -> int:
        return self.min_num
        
