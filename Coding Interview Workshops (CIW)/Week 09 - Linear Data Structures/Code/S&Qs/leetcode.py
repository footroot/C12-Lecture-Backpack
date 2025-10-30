from collections import deque
"""
APC

1. Assumptions
 - int in stack
 - 100 calls to push, pop, top and empty
 - use deque (doubly linked list)


2. Plan 

[9,0,7,8]
 - push (1) -> [1,9,0,7,8]
 - pop () -> [9,0,7,8]

 [] [9,0,7,8] -> 1 -> [1] [9,0,7,8] -> [1,9,0,7,8] []
                   -> [9,0,7,8,1] -> [0,7,8,1,9], [7,8,1,9,0], [8,1,9,0,7], [1,9,0,7,8]

 - enqueue (1) -> [9,0,7,8,1]
 - dequeue () -> [0,7,8,1]


3. Code


"""

class MyStack(object):
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
        self.in_q1 = True

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if (self.in_q1):
            self.q2.append(x)
            while (len(self.q1)>0):
                y = self.q1.popleft()
                self.q2.append(y)
            self.in_q1 = False
        else:
            self.q1.append(x)
            while (len(self.q2)>0):
                y = self.q2.popleft()
                self.q1.append(y)
            self.in_q1 = True

        

    def pop(self):
        """
        :rtype: int
        """
        if (self.in_q1):
            return self.q1.popleft()
        else:
            return self.q2.popleft()
        
        

    def top(self):
        """
        :rtype: int
        """
        if (self.in_q1):
            return self.q1[0]
        else:
            return self.q2[0]
        

    def empty(self):
        """
        :rtype: bool
        """
        if (self.in_q1):
            if len(self.q1) == 0:
                return True
            else:
                return False
        else:
            if len(self.q2) == 0:
                return True
            else:
                return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()