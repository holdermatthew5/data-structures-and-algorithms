def zipLists(list1, list2):
    result = list1
    current1 = list1.head
    current2 = list2.head
    while current1 and current2:
        nxt1 = current1.next
        nxt2 = current2.next
        current1.next = current2
        current2.next = nxt1
        if not nxt2:
            current1.next = current2
        current1 = current1.next.next
        current2 = nxt2
    return result

# Personal stretch:
    # Edge case: list1 is empty
    # Edge case: list2 is empty
    # if not current1 and not current2:
        # raise an empty lists error
    # elif not current1:
        # return current2
    # elif not current2
        # return current1
    # ^^^Raises an error if both lists are empty. If both are not empty checks if one is. If one is empty it returns the opposite list. otherwise it continues to the while loop.^^^
    # ^How would I raise that error? Would I need to create an exception class? Look more into this later.^

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
        Current = self.head
        if Current == None:
            self.head = Node(value)
        while Current:
            if Current.next == None:
                node = Node(value)
                Current.next = node
                return
            else:
                Current = Current.next

    def insertBefore(self, value, newVal):
            Current = self.head
            if Current == None:
                self.head = Node(value)
            elif Current.value == value:
                self.insert(newVal)
                return
            while Current:
                if Current.next.value == value:
                    beforeVal = Current.next
                    Current.next = Node(newVal, beforeVal)
                    return
                elif Current.next.value != value:
                    Current = Current.next
                else:
                    return "EXCEPTION"
            
    def insertAfter(self, value, newVal):
        Current = self.head
        if Current == None:
            self.head = Node(value)
        while Current:
            if Current.value == value:
                afterVal = Current.next
                Current.next = Node(newVal, afterVal)
                return
            elif Current.value != value:
                Current = Current.next
            else:
                return "EXCEPTION"
    
    def kthHelper(self):
        emptyList = []
        Current = self.head
        while Current:
            emptyList.append(Current.value)
            Current = Current.next
        return emptyList

    def kthFromEnd(self, k):
        helper = self.kthHelper()
        length = (len(helper)-1)-k
        if k < len(helper) and k >= 0:
            return helper[length]
        else:
            return "EXCEPTION"    

class Node:

    def __init__(self, value, nxt=None):
        self.value = value
        self.next = nxt