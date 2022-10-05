# SINGLY LINKED LIST 

class Node:
    def __init__ (self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head
        self.length = 1


    def append(self, value):
        newNode = Node(value)
        self.tail.next = newNode
        self.tail = newNode
        self.length +=1

    def prepend(self, value):
        newNode = Node(value)
        newNode.next = self.head
        self.head = newNode 
        self.length +=1 

    def printList(self):
        arr = []    
        curr = self.head
        while (curr is not None):
            arr.append(curr.value)
            curr = curr.next
        print(arr)


    def findNode(self, index):
        curr = self.head
        count = 0
        while count < index:
            curr = curr.next
            count +=1
        return curr


    def insert(self, index, value):
        if index > self.length:
            self.append(value)
        elif index == 0:
            self.prepend(value)
        else:
            newNode = Node(value)
            prev = self.findNode(index-1)
            newNode.next = prev.next
            prev.next = newNode
            self.length +=1

    def remove(self, index):
        if index > self.length:
            prev = self.findNode(self.length-2)
            self.tail = prev
            self.tail.next = None
        elif index == 0:
            new_head = self.head.next
            self.head = new_head
        else:
            prev = self.findNode(index-1)
            prev.next = prev.next.next
        self.length +=1

    def reverse(self):
        if self.length == 0:
            return self.head.vlaue
        else:
            curr = self.head
            self.tail = self.head
            sec_curr = curr.next
            while sec_curr:
                temp = sec_curr.next
                sec_curr.next = curr
                curr = sec_curr
                sec_curr = temp
            self.head.next = None
            self.head = curr
            

# Find a shorter and more explainable way to reverse the list




list = LinkedList(5)
list.append(4)
list.prepend(322)
list.append(2)
list.prepend(109)
# list.printList()
list.insert(5, 110)
# list.printList()
list.remove(8)
list.printList()
list.reverse()
list.printList()

# print(list.length)


