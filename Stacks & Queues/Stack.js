// STACKS WITH LINKEDLIST

class Node {
    constructor(value) {
        this.value = value;
        this.next = null;
    }
}
class LinkedStack {
    constructor() {
        this.top = null;
        this.bottom = null;
        this.length = 0;
    }

    peek() {
        return this.top;

    }
    push(value) {
       const newNode  = new Node(value)
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



// TESTING

const myStack = new LinkedStack();
console.log(myStack.peek());
    myStack.push("google");
    myStack.push("udemy");
    myStack.push("discord");
    console.log(myStack.peek());
    console.log(myStack.pop());
    console.log(myStack.pop());
myStack.pop();
myStack.pop();


// STACKS WITH ARRAYS


class ArrayStack {
    constructor() {
        this.array = [];
    }

    peek(){
        return(this.array[this.array.length-1])
    }

    push(value) {
        this.array.push(value);
        return this;
    }

    pop() {
        this.array.pop();
        return this;
    }
}
 
// TESTING 

const newStack = new ArrayStack();
console.log(newStack.peek());
console.log(newStack.push("google"));
console.log(newStack.push("udemy"));
console.log(newStack.push("discord"));
console.log(newStack.peek());
console.log(newStack.pop());
console.log(newStack.pop());
console.log(newStack.peek()); 