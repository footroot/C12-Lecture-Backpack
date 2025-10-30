
// Simple queue class using Array to define operations
class Queue {
    // Initialise the queue by creating an empty array
    constructor() {
        this.queue = [];
    }

// Add an element to the end of the queue
    enqueue(value) {
        this.queue.push(value);
    }

// Remove an element from the front of the queue
    dequeue() {
        if (this.queue.length === 0) {
            console.log("Error: Queue Underflow!");
            return null;
        } else {
            return this.queue.shift();
        }
    }
}

// Create a queue to test the class
let queue = new Queue();

// Check underflow error
queue.dequeue();
console.log(queue.queue)

// Add some elements to the queue
queue.enqueue(1);
console.log(queue.queue)
queue.enqueue(2);
console.log(queue.queue)
queue.enqueue(945);
console.log(queue.queue)

// Remove an element from the queue
let popped = queue.dequeue();
console.log(`Dequeued element: ${popped}`);

console.log(queue.queue)
