class MinStack:

    def __init__(self):
        self.l = []        

    def push(self, val: int) -> None:
        if len(self.l) == 0:
            mini = val
        else:
            mini = min(self.l[-1][1], val)

        self.l.append((val, mini))
        
    def pop(self) -> None:
        self.l.pop()

    def top(self) -> int:
        return self.l[-1][0]

    def getMin(self) -> int:
        return self.l[-1][1]
        
