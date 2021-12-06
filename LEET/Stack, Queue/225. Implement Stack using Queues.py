#https://leetcode.com/problems/implement-stack-using-queues/
from collections import deque

class MyStack:

    def __init__(self):
        self.q1 = deque()
        
    def push(self, x: int) -> None:
        self.q1.append(x)
        for _ in range(len(self.q1)-1):
            pop_node = self.q1.popleft()
            self.q1.append(pop_node)

    def pop(self) -> int:
        return self.q1.popleft()

    def top(self) -> int:
        return self.q1[0]

    def empty(self) -> bool:
        if not self.q1:
            return True
        return False

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()