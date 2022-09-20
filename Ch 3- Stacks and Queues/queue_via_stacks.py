# Cracking the Coding Interview Q 3.4 Queue Via Stacks

# Use two stacks to implement a queue

# Two ways to do this, one with enQueue as O(N) and deQueue as O(1)
# and another as deQueue as O(N) and enQueue as O(1)

class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enQueue_on(self, x):
        # Greedy enqueue

        while(self.stack1):
            self.stack2.append(self.stack1.pop())

        self.stack1.append(x)

        while(self.stack2):
            self.stack1.append(self.stack2.pop())

    def deQueue_o1(self):
        # Dequeue for greedy Enqueue

        while(self.stack1):
            return self.stack1.pop()
        return None

    def enQueue_o1(self, x):
        # Constant enqueue

        self.stack1.append(x)

    def deQueue_on(self):
        # Greedy enqueue for constant dequeue

        if len(self.stack2) > 0:
            return self.stack2.pop()
        elif len(self.stack1) > 0:
            while(self.stack1):
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()
        else:
            return None


Q = MyQueue()

Q.enQueue_on(1)
Q.enQueue_on(2)
Q.enQueue_on(3)

print(Q.deQueue_o1())
print(Q.deQueue_o1())
print(Q.deQueue_o1())
print(Q.deQueue_o1())

Q.enQueue_o1(10)
Q.enQueue_o1(20)
Q.enQueue_o1(30)

print(Q.deQueue_on())
print(Q.deQueue_on())
print(Q.deQueue_on())
print(Q.deQueue_on())
