# Array-like List Implementation
class CustomArray:
    def __init__(self):
        self.items = []
    
    def remove(self, value):
        """Remove first occurrence of the specified value"""
        self.items.remove(value)
    
    def append(self, value):
        """Add an element to the end of the array"""
        self.items.append(value)
    
    def __setitem__(self, index, value):
        """Allow direct indexing assignment"""
        self.items[index] = value
    
    def __getitem__(self, index):
        """Allow direct indexing access"""
        return self.items[index]
    
    def __str__(self):
        return str(self.items)

# Stack Implementation
class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, value):
        """Add an element to the top of the stack"""
        self.items.append(value)
    
    def pop(self):
        """Remove and return the top element of the stack"""
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty")
    
    def is_empty(self):
        """Check if the stack is empty"""
        return len(self.items) == 0
    
    def __str__(self):
        return str(self.items)

# Queue Implementation
class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, value):
        """Add an element to the back of the queue"""
        self.items.append(value)
    
    def dequeue(self):
        """Remove and return the front element of the queue"""
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Queue is empty")
    
    def is_empty(self):
        """Check if the queue is empty"""
        return len(self.items) == 0
    
    def __str__(self):
        return str(self.items)

# Dictionary Implementation
class CustomDictionary:
    def __init__(self):
        self.items = {}
    
    def __setitem__(self, key, value):
        """Set a key-value pair in the dictionary"""
        self.items[key] = value
    
    def __getitem__(self, key):
        """Get a value by key"""
        return self.items[key]
    
    def __str__(self):
        return str(self.items)

# Demonstration of usage
def demonstrate_data_structures():
    print("Array Operations:")
    arr = CustomArray()
    arr.append(5)
    arr.append(6)
    arr.append(7)
    print("Initial array:", arr)
    
    arr.remove(6)
    print("After removing 6:", arr)
    
    arr[2] = 10
    print("After setting index 2 to 10:", arr)
    
    print("\nStack Operations:")
    stack = Stack()
    stack.push(5)
    stack.push(6)
    print("Stack:", stack)
    
    popped = stack.pop()
    print("Popped value:", popped)
    print("Stack after pop:", stack)
    
    print("\nQueue Operations:")
    queue = Queue()
    queue.enqueue(3)
    queue.enqueue(4)
    print("Queue:", queue)
    
    dequeued = queue.dequeue()
    print("Dequeued value:", dequeued)
    print("Queue after dequeue:", queue)
    
    print("\nDictionary Operations:")
    dict_obj = CustomDictionary()
    dict_obj['key'] = 'new_value'
    print("Dictionary:", dict_obj)