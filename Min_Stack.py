# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# Implement the MinStack class:

# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.

# Solution 
class MinStack:
    def __init__ (self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)
    
    def pop(self):
        self.stack.pop()

    def top(self):
        return(self.stack[-1])

    def getMin(self):
        return min(self.stack)


# Test Cases
myStack = MinStack()

myStack.push(-2)
myStack.push(0)
myStack.push(-3)
print(myStack.getMin())
myStack.pop()
print(myStack.top())
print(myStack.getMin())



