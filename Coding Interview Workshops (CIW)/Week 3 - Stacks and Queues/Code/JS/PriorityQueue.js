
// Simple priority queue class using Array to define operations
class PriorityQueue {
    // Initialise the queue by creating an empty array
    // Every element will be a pair of values 
    constructor() {
        this.pqueue = [];
    }

// Add an element to the end of the queue
// Sort by priority to queue by priority
    enqueue(value, priority) {
        this.pqueue.push([priority,value]);
        this.pqueue.sort(function(a, b) {
            return a[0] - b[0];
        });
    }

// Remove an element from the front of the queue
// The element would be at the end of list but
// the beginning of our queue
    dequeue() {
        if (this.pqueue.length === 0) {
            console.log("Error: Queue Underflow!");
            return null;
        } else {
            return this.pqueue.pop();
        }
    }
}

// Create a priority queue to test the class
let pqueue = new PriorityQueue();

// Check underflow error
pqueue.dequeue();

// Add some elements to the priority queue
pqueue.enqueue(1, 90);
pqueue.enqueue(2, 100);
pqueue.enqueue(945, 95);

// Remove an element from the priority queue
let popped = pqueue.dequeue();
console.log(`Dequeued element: ${popped}`);
