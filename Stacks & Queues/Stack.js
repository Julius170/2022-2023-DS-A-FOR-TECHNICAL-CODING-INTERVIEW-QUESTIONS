// STACKS WITH LINKEDLIST

class Node {
    constructor(value) {
        this.value = value;
        this.next = null;
    }
}
class Stack {
    constructor() {
        this.top = null;
        this.bottom = null;
        this.length = 0;
    }

    peek() {
        return this.top;

    }
    push(value) {
       const newNode  = new Node
       newNode.value = value 
       if (this.length === 0) {
            this.top = newNode;
            this.bottom = newNode;
        } else {
            const holdingPotinter = this.top;
            this.top = newNode
            this.top.next = holdingPotinter;
        }
        this.length++;
        return this;
    }
    pop() {
        if (!this.top) {
            return null;
        }
        if (this.length === 1) {
            this.top = null;
            this.bottom = null;
        }
        this.top = this.top.next;
        this.length--;
        return this

    }
}





const myStack = new Stack();
console.log(myStack.peek());
    myStack.push("google");
    myStack.push("udemy");
    myStack.push("discord");
    console.log(myStack.peek());
    console.log(myStack.pop());
    console.log(myStack.pop());
    // myStack.pop();
    // myStack.pop();


// STACKS WITH ARRAYS

