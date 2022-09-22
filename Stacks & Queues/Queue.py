# QUEUES WITH LINKED LIST

class Node:
    def __init__ (self, value):
        self.value = value
        self.next = None
    

class LinkedQueue:
    def __init__ (self):
        self.first = None
        self.last = None
        self.length = 0

    def isEmpty(self):
        if self.first == None:
            return True
        else: return False

    def peek(self):
        return self.last.value
    
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
        self.length +=1
        return self.last.value

    def dequeue(self):
        if not self.first:
            return "Queue is Empty"
        elif self.first == self.last:
            self.first = None
            self.last = None
            return "Queue is Empty"
        else:
            # firstNode = self.first
            self.first = self.first.next
            # firstNode = None
        self.length -=1
        return self.first



# TESTING

# myQueue = LinkedQueue()
# print(myQueue.isEmpty())
# print(myQueue.peek())
# print(myQueue.enqueue("Lovelle"))
# print(myQueue.enqueue("Jade"))
# print(myQueue.enqueue("Saphir"))
# print(myQueue.dequeue())
# print(myQueue.peek()) 