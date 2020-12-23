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
    
    def append(self, value):
        current = self.head
        if current == None:
            self.head = Node(value)
        while current:
            if current.nextNodeValue == None:
                node = Node(value)
                current.nextNodeValue = node
                return
            else:
                current = current.nextNodeValue

    def insertBefore(self, value, newVal):
            current = self.head
            if current == None:
                self.head = Node(value)
            elif current.nodeValue == value:
                self.insert(newVal)
                return
            while current:
                if current.nextNodeValue.nodeValue == value:
                    beforeVal = current.nextNodeValue
                    current.nextNodeValue = Node(newVal, beforeVal)
                    return
                elif current.nextNodeValue.nodeValue != value:
                    current = current.nextNodeValue
                else:
                    return "EXCEPTION"
            
    def insertAfter(self, value, newVal):
        current = self.head
        if current == None:
            self.head = Node(value)
        while current:
            if current.nodeValue == value:
                afterVal = current.nextNodeValue
                current.nextNodeValue = Node(newVal, afterVal)
                return
            elif current.nodeValue != value:
                current = current.nextNodeValue
            else:
                return "EXCEPTION"

class Node:

    def __init__(self, value, next=None):
        self.value = value
        self.next = next