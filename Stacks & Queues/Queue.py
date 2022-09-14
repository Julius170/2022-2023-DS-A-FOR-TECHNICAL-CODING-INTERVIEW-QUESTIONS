# QUEUES WITH LINKED LIST

class Node:
    def __init__ (self, value):
        self.valaue = value
        self.next = None
    

class LinkedQueue:
    def __init__ (self):
        self.first = None
        self.last = None
        self.length = 0

    def isEmpty(self):
        if self.first == None:
            return False
        else: return True

    def peek(self):
        return self.last
    
    def enqueue(self, value):
        newNode = Node(value)
        if self.isEmpty() == True:
            self.first = newNode
            self.last = newNode
        elif self.first == self.last:
            self.first.next == newNode
            self.last = newNode
        else:
            self.last.next == newNode
            self.last = newNode
        
        return self

    def dequeue(self):
        if self.isEmpty() == True:
            return "Queue is already Empty"
        elif self.first == self.last:
            self.first = None        
            self.last = None
        else:
            firstNode = self.first
            self.first = self.first.next
            firstNode = None

        return self



         


        
