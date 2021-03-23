from hashtable.linked_list import Node, LinkedList
from hashtable.hashtable import Hash

def left_join(left, right):
    keys = []
    if not left.table and not right.table:
        return
    elif not left.table:
        return right
    elif not right.table:
        return left
    else:
        for ll in right.table:
            if not ll.head: # might error out when .head is None
                continue
            current = ll.head
            while current:
                keys.append(current.data[0])
                current = current.next
        for ll in left.table:
            if not ll.head:
                continue
            current = ll.head
            while current:
                if current.data[0] in keys:
                    current.data.append(right.get(current.data[0]))
                current = current.next
    return left