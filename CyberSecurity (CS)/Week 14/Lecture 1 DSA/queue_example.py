class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return None  # Queue is empty

    def is_empty(self):
        return len(self.queue) == 0

    def peek(self):
        return self.queue[0] if not self.is_empty() else None


q = Queue()
q.enqueue(1)
q.enqueue(2)
print(q.peek())
print(q.dequeue())
print(q.peek())
print(q.dequeue()) 
