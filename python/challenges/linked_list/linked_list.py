class linked_list:

    def __init__(self, head, values=None):
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
        while Current.next is not None:
            string = f'{string} -> {Current.value}'

class Node:

    def __init__(self, value, next=None):
        self.value = value
        self.next = next