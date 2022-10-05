# Doubly Linked List

class Node:
   def __init__(self, value):
      self.value = value
      self.next = None
      self.prev = None

class doublyLinkedList:
    def __init__(self, value):
      self.head = Node(value)
      self.tail = self.head
      self.length = 1

    def isEmpty(self):
        if self.head == self.tail:
            return True
        return False

# Adding value elements		
    def append(self, value):
        newNode = Node(value)
        self.tail.next = newNode
        newNode.prev = self.tail
        self.tail = newNode
        self.length += 1


    def prepend(self, value):
        newNode = Node(value)
        self.head.prev = newNode
        newNode.next = self.head
        self.head = newNode
        self.length +=1


# Print the Doubly Linked list		
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
            index_po = self.findNode(index-1)
            node_after = index_po.next
            newNode.next = node_after
            node_after.prev = newNode
            index_po.next = newNode
            newNode.prev = index_po
            self.length +=1


    def remove(self, index):
        if index >= self.length:
            self.tail = self.tail.prev
            self.tail.next = None
        if index == 0:
            self.head = self.head.next
            self.head.prev = None
        if index >0 and index < self.length:
            rem = self.findNode(index)
            node_before = rem.prev
            node_after = rem.next
            node_before.next = node_after
            node_after.prev = node_before
        self.length -=1


        


        

dllist = doublyLinkedList(17)
dllist.append(12)
dllist.append(8)
dllist.prepend(62)
dllist.insert(2, 555)
dllist.printList()
dllist.remove(0)
dllist.printList()
print(dllist.length)







    


