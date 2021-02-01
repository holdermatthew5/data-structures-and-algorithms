def InvalidOperationError(BaseException):
    pass

class InvalidOperationError(BaseException):
    pass

class AnimalShelter():
    """
        Houses dogs and cats.
    """
    def __init__(self):
        self.dogs = PseudoQueue()
        self.cats = PseudoQueue()
    
    def enqueue(self, animal=None):
        if animal.lower() == 'cat':
            self.cats.enqueue(Node('cat'))
        elif animal.lower() == 'dog':
            self.dogs.enqueue(Node('dog'))
        else:
            raise InvalidOperationError("Please submit a dog or a cat.")
    
    def dequeue(self, preference=None):
        if preference.lower() == 'cat':
            return self.cats.dequeue()
        elif preference.lower() == 'dog':
            return self.dogs.dequeue()
        else:
            return NULL

class PseudoQueue():
    """
        Manages up to 2 stacks in a queue.
    """
    def __init__(self):
        self.front = None
        self.rear = None
    
    def enqueue(self, value):
        if self.front and self.rear:
            raise InvalidOperationError("Method not allowed on full queue.")
        elif self.front and not self.rear:
            self.rear = value
        elif self.rear and not self.front:
            self.front = self.rear
            self.rear = None
        else:
            self.front = value
    
    def dequeue(self):
        if self.front and self.rear:
            stack = self.front
            self.front = self.rear
            self.rear = None
            return stack
        elif self.front and not self.rear:
            stack = self.front
            self.front = None
            return stack
        else:
            raise InvalidOperationError("Method not allowed on empty queue.")

class Stack():
    """
        Manages a stack of nodes.
    """
    def __init__(self, node=None):
        self.top = node
    
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
    
class Node():
    """
        Instantiates a node to be pushed into a stack.
    """
    def __init__(self, value=None):
        self.value = value
        self.next = None