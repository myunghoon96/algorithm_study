#https://leetcode.com/problems/design-circular-queue/

class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [None]*k
        self.front = 0
        self.rear = 0
        
    def enQueue(self, value: int) -> bool:
        if self.q[self.rear]==None:
            self.q[self.rear]=value
            self.rear+=1
            self.rear%=len(self.q)
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if self.q[self.front]!=None:
            self.q[self.front]=None
            self.front+=1
            self.front%=len(self.q)
            return True
        else:
            return False

    def Front(self) -> int:
        if self.front == self.rear and self.q[self.front]==None:
            return -1
        return self.q[self.front]

    def Rear(self) -> int:
        if self.rear==0:
            last_index = (len(self.q)-1)
        else:
            last_index = self.rear-1
        
        if self.q[last_index]==None:
            return -1
        
        else:
            return self.q[last_index]
      
    def isEmpty(self) -> bool:
        if self.front == self.rear and self.q[self.front]==None:
            return True
        else:
            return False    

    def isFull(self) -> bool:
        for i in range(len(self.q)):
            if self.q[i]==None:
                return False
        return True
# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()