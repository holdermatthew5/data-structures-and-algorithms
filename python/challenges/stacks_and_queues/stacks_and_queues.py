class InvalidOperationError(BaseException):
    pass

class Node():
    """
        Instantiates a node to be pushed into a stack.
    """
    def __init__(self, value=None):
        self.value = value
        self.next = None
    
class Stack():
    """
        Manages a stack of nodes.
    """
    def __init__(self):
        self.top = None
    
    def push(self, value):
        current = self.top
        self.top = Node(value)
        self.top.next = current
    
    def pop(self):
        if self.top != None:
            current = self.top
            nxt = self.top.next
            self.top = nxt
            return current
        else:
            raise InvalidOperationError("Method not allowed on empty collection.")
    
    def peek(self):
        if self.top == None:
            raise InvalidOperationError("Method not allowed on empty collection.")
        else:
            return self.top.value
    
    def is_empty(self):
        if self.top == None:
            return True
        else:
            return False
    
class Queue():
    """
        Manages nodes in a Queue.
    """
    def __init__(self):
        self.front = None
        self.rear = None
    
    def enqueue(self, value):
        if not self.front and not self.rear:
            self.rear = Node(value)
            self.front = self.rear
        else:
            rear = self.rear
            new = Node(value)
            new.next = rear
            self.rear = new
    
    def dequeue(self):
        if not self.front and not self.rear:
            raise InvalidOperationError("Method not allowed on empty collection.")
        else:
            front = self.front
            rear = self.rear
            while rear.next.next != None:
                rear = rear.next
            self.front = rear
            return front

    def peek(self):
        if self.rear != None:
            return self.rear.value
        else:
            raise InvalidOperationError("Method not allowed on empty collection.")

    def is_empty(self):
        if not self.rear and not self.front:
            return True
        else:
            return False