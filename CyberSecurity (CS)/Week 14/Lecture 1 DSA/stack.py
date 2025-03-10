class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None  # Stack is empty

    def is_empty(self):
        return len(self.stack) == 0

    def peek(self):
        return self.stack[-1] if not self.is_empty() else None

s = Stack()
s.push(10)
s.push(20)
print(s.pop())# Output: 20
print(s.peek())  
