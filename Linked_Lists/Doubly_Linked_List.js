class Node {
  constructor(value) {
    this.value = value,
    this.next = null,
    this.prev = null

  }
}

class DoublyLinkedList {
  constructor(value) {
    this.head = {
      value: value,
      next: null,
      prev : null
    };

    this.tail = this.head;
    this.length = 1;
  }

  append(value) {
    const newNode = new Node(value);

    this.tail.next = newNode;
    newNode.prev = this.tail;
    this.tail = this.tail.next; // newNode
    this.length++;
    return this;
  }
  prepend(value) {
    const newNode = new Node(value);
    newNode.next = this.head;
    this.head.prev  = newNode;
    this.head = newNode;
    this.length++;
    return this;
  }

  printList() {
    const array = [];
    let currentNode = this.head;
    while (currentNode !== null) {
      array.push(currentNode.value);
      currentNode = currentNode.next;
    }
    return array;
  }

  insert(index, value) {
    if (index >= this.length) {
      return this.append(value);
    }
    if (index === 0) {
      this.prepend(value);
    }
    const newNode = new Node(value);
    let nod = this.head;
    let count = 0;
    while (count < index - 1) {
      nod = nod.next;
      count++;
      if (count == index - 1) {
        const holder = nod.next;
        holder.prev = newNode;
        newNode.next = holder;
        newNode.prev = nod
        nod.next = newNode;
      }
    }
    this.length++;
    return this;
  }
  remove(index) {
    if (index > this.length) {
        return `index ${index} is out of bound`;
    }
    if (index === 0) {
      this.head == this.head.next;
      this.head.prev = null;
      return this;
    }
    let count = 0;
    let nod = this.head;
    while (count < index - 1) {
      nod = nod.next;
      count++;
    }
    if (count == index - 1) {
      const after = nod.next.next;
      nod.next = after;
      if (after != null) {
          after.prev = nod;
      }
    }
    this.length--;
    return this;
  }
}

const myLinkedList = new DoublyLinkedList(10);

myLinkedList.append(5);
myLinkedList.append(16);
myLinkedList.prepend(1);
myLinkedList.insert(2, 20);
myLinkedList.insert(20, 100);
myLinkedList.insert(0, 100);
console.log(myLinkedList.remove(6));
console.log(myLinkedList.printList());

// console.log(myLinkedList)
