import pytest
from linked_list import LinkedList, Node

def test_linked_list(linked_list):
    assert linked_list

def test_insert(linked_list):
    assert linked_list.head.value == 'd'

def test_next(linked_list):
    assert linked_list.head.next.value == 'c'

def test_includes_true(linked_list):
    assert linked_list.includes('a')

def test_includes_false(linked_list):
    assert not linked_list.includes('e')

def test_string(linked_list):
    assert linked_list.__str__() == 'd -> c -> b -> a'

def test_append():
    appendList = LinkedList()
    appendList.insert("THR33")
    appendList.insert("TOO")
    appendList.insert("WON")
    appendList.append("FOR")
    actual = [appendList.head.value, appendList.head.next.value, appendList.head.next.next.value, appendList.head.next.next.next.value]
    expected = ["WON", "TOO", "THR33", "FOR"]
    assert actual == expected

def test_multiple_append():
    multipleAppendList = LinkedList()
    multipleAppendList.insert("THR33")
    multipleAppendList.insert("TOO")
    multipleAppendList.insert("WON")
    multipleAppendList.append("FOR")
    multipleAppendList.append("F1V3")
    actual = [multipleAppendList.head.value, multipleAppendList.head.next.value, multipleAppendList.head.next.next.value, multipleAppendList.head.next.next.next.value, multipleAppendList.head.next.next.next.next.value]
    expected = ["WON", "TOO", "THR33", "FOR", "F1V3"]
    assert actual == expected

def test_insert_before_value():
    insertBeforeList = LinkedList()
    insertBeforeList.insert("THR33")
    insertBeforeList.insert("TOO")
    insertBeforeList.insert("WON")
    insertBeforeList.insertBefore("TOO", "INSERTER")
    actual = [insertBeforeList.head.value, insertBeforeList.head.next.value, insertBeforeList.head.next.next.value, insertBeforeList.head.next.next.next.value]
    expected = ["WON", "INSERTER", "TOO", "THR33"]
    assert actual == expected

def test_insert_before_head_value():
    insertBeforeList = LinkedList()
    insertBeforeList.insert("THR33")
    insertBeforeList.insert("TOO")
    insertBeforeList.insert("WON")
    insertBeforeList.insertBefore("WON", "Z3R0")
    actual = [insertBeforeList.head.value, insertBeforeList.head.next.value, insertBeforeList.head.next.next.value, insertBeforeList.head.next.next.next.value]
    expected = ["Z3R0", "WON", "TOO", "THR33"]
    assert actual == expected

def test_insert_in_middle_value():
    insertToMiddle = LinkedList()
    insertToMiddle.insert("THR33")
    insertToMiddle.insert("TOO")
    insertToMiddle.insert("WON")
    insertToMiddle.insertAfter("WON", "FORE")
    actual = [insertToMiddle.head.value, insertToMiddle.head.next.value, insertToMiddle.head.next.next.value, insertToMiddle.head.next.next.next.value]
    expected = ["WON", "FORE", "TOO", "THR33"]
    assert actual == expected

def test_insert_to_end_value():
    insertToEnd = LinkedList()
    insertToEnd.insert("THR33")
    insertToEnd.insert("TOO")
    insertToEnd.insert("WON")
    insertToEnd.insertAfter("THR33", "FORE")
    actual = [insertToEnd.head.value, insertToEnd.head.next.value, insertToEnd.head.next.next.value, insertToEnd.head.next.next.next.value]
    expected = ["WON", "TOO", "THR33", "FORE"]
    assert actual == expected

def test_greater_than_list_length():
    happy_pants = LinkedList()
    happy_pants.insert(2)
    happy_pants.insert(8)
    happy_pants.insert(3)
    happy_pants.insert(1)
    actual = happy_pants.kthFromEnd(10)
    expected = "EXCEPTION"
    assert actual == expected

def test_k_equals_list_length():
    happy_pants = LinkedList()
    happy_pants.insert(2)
    happy_pants.insert(8)
    happy_pants.insert(3)
    happy_pants.insert(1)
    actual = happy_pants.kthFromEnd(4)
    expected = "EXCEPTION"
    assert actual == expected

def test_k_is_a_negative_number():
    happy_pants = LinkedList()
    happy_pants.insert(2)
    happy_pants.insert(8)
    happy_pants.insert(3)
    happy_pants.insert(1)
    actual = happy_pants.kthFromEnd(-2)
    expected = "EXCEPTION"
    assert actual == expected

def test_list_length_equals_1():
    happy_pants = LinkedList()
    happy_pants.insert(2)
    actual = happy_pants.kthFromEnd(0)
    expected = 2
    assert actual == expected
    
def test_happy_pants_kth_value():
    happy_pants = LinkedList()
    happy_pants.insert(2)
    happy_pants.insert(8)
    happy_pants.insert(3)
    happy_pants.insert(1)
    actual = happy_pants.kthFromEnd(2)
    expected = 3
    assert actual == expected

@pytest.fixture
def linked_list():
    new_linked_list = LinkedList()
    new_linked_list.insert('a')
    new_linked_list.insert('b')
    new_linked_list.insert('c')
    new_linked_list.insert('d')
    return new_linked_list