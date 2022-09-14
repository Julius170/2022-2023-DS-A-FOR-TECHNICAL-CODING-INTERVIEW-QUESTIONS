// QUEUES USING LINKED LIST

class Node {
    constructor(value) {
        this.value = value;
        this.next = null;
    }
} 

class Queue {
    constructor() {
        this.first = null;
        this.last  = null;
        this.length = 0;
    }
    isEmpty(){
        if (this.first === null){
            return true
        }else {
            return false
        }

    }
    peek() {
        if (this.isEmpty() === true){
            return "Queue is Empty"
        }else{
            return this.first;
        }
    }
    enqueue(value) {
        const newNode = new Node(value);
        newNode.value = value
        if (this.length === 0) {
            this.first = newNode;
            this.last = newNode;
        }else {
            this.last.next = newNode
            this.last = newNode
        }
        this.length++;
        return this
    }
    dequeue() {
        if (!this.first){
            return ("Queue is empty")
        }
        if (this.first == this.next) {
            this.last = null 
        }
        this.first = this.first.next 
        this.length--;
        return this
    }
}

// TESTING 
const myQueue = new Queue()
console.log(myQueue.peek())
console.log(myQueue.enqueue("Joy"))
console.log(myQueue.enqueue("Kelvin"))
console.log(myQueue.enqueue("Collins"))
console.log(myQueue.enqueue("Carlos"))
console.log(myQueue.enqueue("Logan"))
console.log(myQueue.dequeue());
console.log(myQueue.dequeue());
console.log(myQueue.dequeue());