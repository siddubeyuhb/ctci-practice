# Cracking the Coding Interview Q 3.2 Stack Min

# Implement a stack with push, pop and min functions
# which all operate in O(1) time

# We are storing MinVal for every push operation as a
# tuple with the input value, after comparing with previous
# min value

class StackMin:

    def __init__(self):
        self.stack = []

    def pop(self):
        if(len(self.stack)) == 0:
            return None
        return self.stack.pop()[0]

    def push(self, value):
        minVal = self.min()

        if minVal is None or minVal > value:
            minVal = value

        self.stack.append((value, minVal))

    def min(self):
        if(len(self.stack)) == 0:
            return None
        return self.stack[-1][1]


sta = StackMin()
sta.push(5)
sta.push(2)
sta.push(10)
print(sta.min())
sta.push(1)
print(sta.pop())
