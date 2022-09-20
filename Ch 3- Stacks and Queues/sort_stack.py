# Cracking the Coding Interview Q 3.5 Sort Stack

# Sort a stack in ascending order using only another temp stack
# Stack class supports push, pop, peek and isEmpty(bool) operations

def SortStack(stack):
    tempStack = Stack()

    while(stack.peek()):
        temp = stack.peek()
        stack.pop()

        while(tempStack.isEmpty() == False and
                int(tempStack.peek()) > int(temp)):

            stack.push(tempStack.peek())
            tempStack.pop()

        tempStack.push(temp)
    return tempStack

    # New_stack for descending order instead of ascending
    new_stack = Stack()
    while(tempStack.peek()):

        new_stack.push(tempStack.peek())
        tempStack.pop()
    return new_stack


class Stack:

    def __init__(self):
        self.stack = []

    def rev(self):
        return self.stack[::-1]

    def push(self, x):
        self.stack.append(x)

    def pop(self):

        if(len(self.stack) == 0):
            return None
        return self.stack.pop()

    def peek(self):

        if(len(self.stack) == 0):
            return None
        return self.stack[-1]

    def isEmpty(self):

        if(len(self.stack) == 0):
            return True
        return False


########
# Tests
########
k = Stack()
k.push(17), k.push(21), k.push(3), k.push(8)

print(k.stack)
new = SortStack(k)
print(new.stack)

new.push(1)
new.push(100)
new.push(12)
print(new.stack)
new = SortStack(new)
print(new.stack)
