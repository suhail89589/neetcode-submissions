class MyQueue:

    def __init__(self):
        self.s1 = []
        self.queve = []

        

    def push(self, x: int) -> None:
        self.s1.append(x)

        

        

    def pop(self) -> int:
        if not self.queve:
            while self.s1:
                self.queve.append(self.s1.pop())
        return self.queve.pop()
        

    def peek(self) -> int:
        if not self.queve:
            while self.s1:
                self.queve.append(self.s1.pop())
        return self.queve[-1]
        

    def empty(self) -> bool:
        return max(len(self.s1), len(self.queve)) ==  0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()