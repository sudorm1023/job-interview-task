class CQueue:

    def __init__(self):
        self.A = []
        self.B = []


    def appendTail(self, value: int) -> None:
        self.A.append(value)


    def deleteHead(self) -> int:
        if not self.A and not self.B:
            return -1
        
        if self.B:
            return self.B.pop()
        
        if self.A:
            self.A, self.B = self.B, self.A[::-1]
            return self.B.pop()



# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()