# Simple queue class using deque to define operations
from collections import deque

class Queue:
    # Initialise the queue by creating a deque
    # A queue can be created of fixed length as well
    def __init__(self):
        self.queue = deque()

    # Add an element to the end of the queue
    def enqueue(self, value):
        self.queue.append(value)

    # Remove an element from the front olf the queue
    def dequeue(self):
        if len(self.queue) == 0:
            print("Error: Queue Underflow!")
            return None
        else:
            return self.queue.popleft()
    
# Create a queue to test the class
queue = Queue()

# Check underflow error
queue.dequeue()
print(queue.queue)

# Add some elements to the queue
queue.enqueue(1)
print(queue.queue)
queue.enqueue(2)
print(queue.queue)
queue.enqueue(945)
print(queue.queue)

# Remove an element from the queue
popped = queue.dequeue()
print("Dequeued element: {}".format(popped))
print(queue.queue)