#https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue:

    def __init__(self):
        self.stack = []
        self.stack2 = []
        
    def push(self, x: int) -> None:
        self.stack.append(x)
        
    def pop(self) -> int:
        
        while len(self.stack) >1:
            pop_node = self.stack.pop()
            self.stack2.append(pop_node)
               
        first_node = self.stack.pop()
        
        while self.stack2:
            pop_node = self.stack2.pop()
            self.stack.append(pop_node)
        
        return first_node

    def peek(self) -> int:
        return self.stack[0]

    def empty(self) -> bool:
        if not self.stack:
            return True
        
        return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()