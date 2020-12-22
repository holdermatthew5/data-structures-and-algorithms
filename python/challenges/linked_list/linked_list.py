class LinkedList:

    def __init__(self, values=None):
        self.head = None
    
    def insert(self, value):
        node = Node(value)
        if self.head:
            node.next = self.head
        self.head = node
    
    def includes(self, value):
        Current = self.head
        while Current.value is not value:
            if Current.next is None:
                return False
            else:
                Current = Current.next
        return True
    
    def __str__(self):
        Current = self.head
        string = ''
        while not Current.next == None:
            string = f'{string}{Current.value} -> '
            Current = Current.next
        return f'{string}{Current.value}'

class Node:

    def __init__(self, value, next=None):
        self.value = value
        self.next = next