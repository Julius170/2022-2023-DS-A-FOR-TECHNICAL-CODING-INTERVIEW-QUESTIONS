# STACKS WITH LINKED-LIST

class Node:
    def __init__ (self, value):
        self.value = value
        self.next = None



class LinkedStacks:
    def __init__ (self):
        self.top = None
        self.length = 0

    def isEmpty(self):
        if self.length == 0:
            return True # Meaning stack is empty
        else:
            return False # Stack is not empty

    def peek(self):
        if self.isEmpty() == True:
            return "Stack is Empty"
        else:
            return self.top.value

    def push(self, value):
        
        if self.top is None:
            self.top = Node(value)
        else: 
            newNode = Node(value)
            newNode.next = self.top
            self.top = newNode
        
        self.length +=1
        print(self.top.value)
        return self.top.value

    def pop(self):
        if not self.top:
            return (None)
        elif self.length == 1:
            self.top = None
        else:
            popped_node = self.top
            self.top = self.top.next
            popped_node.next = None
        self.length -=1
        return self.top.value
    
    
 




# TESTING

if __name__  ==  "__main__":
    myStack = LinkedStacks()
    print(myStack.peek())
    print(myStack.push("google"))
    print(myStack.push("udemy"))
    print(myStack.push("discord"))
    print(myStack.pop())
    print(myStack.pop())
    print(myStack.pop())
    print(myStack.peek())

# STACKS WITH ARRAYS

# class Stack:
#     def __init__(self):
#         self.array = []

#     def peek(self):
#         print(self.array[len(self.array)-1])
#         return self

#     def push(self, value):
#         self.array.push(value)
#         return self
    
#     def pop(self):
#         self.array.pop()
#         return self
